from selenium.webdriver.common.by import By

class CartElements:
        PRODUCT_LINK = (By.XPATH, "//div[contains(@class,'product-layout')]//a[.//img[@title='{product_name}']]")
        PRODUCT_IMAGE = (By.XPATH, "//img[@title='{product_name}'][@alt='{product_name}']")
        PRODUCT_TITLE = (By.XPATH, "//h4/a[contains(text(),'{product_name}')]")
        
        ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[class*='btn-buynow']")
        CART_ITEMS = (By.CSS_SELECTOR, "div.cart-item")
    
        CART_ITEM_TITLE = (By.XPATH, "//img[@alt='{product_name}' and @title='{product_name}']")
        CART_ITEM_QUANTITY = (By.CSS_SELECTOR, "input.cart-item-quantity")
        CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.btn-primary[href*='checkout']")
    
        SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success")
        CART_EMPTY_MESSAGE = (By.XPATH, "//p[contains(., 'Your shopping cart is empty')]")