from selenium.webdriver.common.by import By

class ProductElements:
    # Elementos da página de resultados de busca
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.product-layout")
    PRODUCT_LINK = (By.CSS_SELECTOR, "div.caption h4 a")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "div.image a img")
    
    # Elementos da página do produto
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product-title")
    ADD_TO_CART_BTN = (By.ID, "button-cart")