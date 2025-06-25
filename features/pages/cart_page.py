from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from features.elements.cart_elements import CartElements
from features.elements.search_elements import SearchElements
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.elements = CartElements()  # Renomeado para 'elements' para melhor semântica

    def click_product(self, product_name):
        """Abordagem alternativa para clicar no produto"""
        try:
            # Primeiro localize todos os produtos
            products = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "div.product-layout")
                )
            )
            
            # Encontre o produto correto
            for product in products:
                try:
                    title = product.find_element(By.CSS_SELECTOR, "h4 a").text
                    if product_name.lower() in title.lower():
                        # Clica via JavaScript para evitar problemas de overlay
                        link = product.find_element(By.TAG_NAME, "a")
                        self.driver.execute_script("arguments[0].click();", link)
                        time.sleep(1)
                        return
                except:
                    continue
                    
            raise Exception(f"Produto '{product_name}' não encontrado na lista")
            
        except Exception as e:
            self.driver.save_screenshot(f"click_product_alt_{product_name}_error.png")
            raise Exception(f"Falha ao clicar no produto (alternativa): {str(e)}")

    def add_to_cart(self):
        """Adiciona o produto atual ao carrinho"""
        try:
            add_button = self.wait.until(
                EC.element_to_be_clickable(self.elements.ADD_TO_CART_BTN)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", add_button)
            add_button.click()
            time.sleep(1)  # Espera para atualização do carrinho
        except Exception as e:
            self.driver.save_screenshot("add_to_cart_error.png")
            raise Exception(f"Falha ao adicionar ao carrinho: {str(e)}")

    def verify_product(self):
       try:
        (EC.visibility_of_element_located(self.elements.CART_ITEM_TITLE))
        time.sleep(1)
       except Exception as e:
            raise Exception(f"Falha ao verificar produto: {str(e)}")
       
       