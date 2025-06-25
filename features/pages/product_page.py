from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from features.elements.product_elements import ProductElements
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.elements = ProductElements()

    def click_product_by_name(self, product_name):
        """Clica no produto com o nome especificado"""
        try:
            # Espera os resultados carregarem
            self.wait.until(
                EC.presence_of_all_elements_located(self.elements.SEARCH_RESULTS)
            )
            time.sleep(1)  # Espera adicional
            
            # Encontra todos os produtos
            products = self.driver.find_elements(*self.elements.SEARCH_RESULTS)
            
            for product in products:
                try:
                    title = product.find_element(*self.elements.PRODUCT_LINK).text
                    if product_name.lower() in title.lower():
                        # Clica no link do produto
                        link = product.find_element(*self.elements.PRODUCT_LINK)
                        self.driver.execute_script("arguments[0].scrollIntoView();", link)
                        self.driver.execute_script("arguments[0].click();", link)
                        return True
                except:
                    continue
            
            raise Exception(f"Produto '{product_name}' não encontrado")
            
        except Exception as e:
            self.driver.save_screenshot(f"click_product_error_{product_name}.png")
            raise Exception(f"Falha ao clicar no produto: {str(e)}")