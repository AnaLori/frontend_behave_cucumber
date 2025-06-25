from selenium.webdriver.common.by import By

class SearchElements:
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = [
        (By.CSS_SELECTOR, "button[type='submit'].type-text"),  # Tentativa principal
        (By.XPATH, "//form[contains(@id,'search')]//button[@type='submit']"),  # Alternativa 1
        (By.XPATH, "//button[contains(@class,'btn') and contains(text(),'Search')]"),  # Alternativa 2
        (By.CSS_SELECTOR, "div.search-button > button"),  # Alternativa 3
        (By.ID, "search-btn")  # Caso exista um ID
    ]
    PRODUCT_THUMBS = (By.CSS_SELECTOR, ".product-layout.product-grid")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, "#entry_212469 > p")