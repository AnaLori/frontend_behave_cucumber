from selenium.webdriver.common.by import By

class LoginElements:
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    MY_ACCOUNT_TITLE = (By.CSS_SELECTOR, "div[id='content'] h2:first-child")