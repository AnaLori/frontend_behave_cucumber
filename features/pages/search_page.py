from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.elements.search_elements import SearchElements
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from features.pages.product_page import ProductPage

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Aumentado para 15 segundos
        self.locators = SearchElements()

    def _find_search_input(self):
        """Localiza o campo de busca com tratamento de erros"""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.locators.SEARCH_INPUT)
            )
        except TimeoutException:
            raise NoSuchElementException("Campo de busca não encontrado")    

    def _find_search_button(self):
        """Tenta encontrar o botão usando múltiplas estratégias"""
        for locator in SearchElements.SEARCH_BUTTON:
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                return element
            except (TimeoutException, NoSuchElementException):
                continue
        raise NoSuchElementException("Não foi possível localizar o botão de busca com nenhum seletor")

    def search(self, product):
        """Preenche o campo de busca e realiza a pesquisa"""
        try:
            # 1. Fechar dropdowns que possam estar atrapalhando
            self.driver.execute_script(
                "document.querySelectorAll('.dropdown.open').forEach(d => d.classList.remove('open'))"
            )
            
            # 2. Localizar e preencher o campo de busca
            search_input = self._find_search_input()
            search_input.clear()
            
            # Digitação lenta para evitar problemas em campos dinâmicos
            for char in product:
                search_input.send_keys(char)
                time.sleep(0.05)  # Pequena pausa entre caracteres
            
            # 3. Localizar e clicar no botão de busca
            search_button = self._find_search_button()
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_button)
            self.driver.execute_script("arguments[0].click();", search_button)
            
            # 4. Espera para carregamento dos resultados
            time.sleep(1)  # Espera implícita para resultados
            
        except Exception as e:
            self.driver.save_screenshot("search_error.png")
            raise Exception(f"Falha na busca por '{product}': {str(e)}")

    def wait_for_results(self, timeout=10):
        """Espera até que os resultados de busca estejam visíveis"""
        try:
            self.wait.until(
                EC.visibility_of_any_elements_located(self.locators.PRODUCT_THUMBS)
            )
            return True
        except:
            return False

    def has_results(self):
        """Verificação robusta de resultados"""
        try:
            products = self.wait.until(
                EC.presence_of_all_elements_located(("css selector", ".product-layout"))
            )
            return len(products) > 0
        except:
            return False

    def no_results_message_visible(self):
        """Verifica se a mensagem de 'nenhum resultado' está visível"""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.locators.NO_RESULTS_MESSAGE)
            ).is_displayed()
        except:
            return False
        
    def verify_search_results(self, expected_has_results=True):
        """Verifica os resultados conforme esperado"""
        if expected_has_results:
            assert self.has_results(), "There is no product that matches the search criteria."
        else:
            assert self.no_results_message_visible(), "Mensagem de 'sem resultados' não encontrada"

    def click_product(self, product_name):
        """Clica no produto específico após busca"""
        try:
            product_link = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//div[contains(@class,'product-layout')]//*[contains(text(), '{product_name}')]")
                )
            )
            product_link.click()
            time.sleep(1)  # Espera para carregamento
            return ProductPage(self.driver)  # Se você tiver uma ProductPage
        except Exception as e:
            self.driver.save_screenshot("click_product_error.png")
            raise Exception(f"Falha ao clicar no produto '{product_name}': {str(e)}")        