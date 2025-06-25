from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.elements.login_elements import LoginElements

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locators = LoginElements

    def open(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        return self

    def enter_email(self, email):
        email_field = self.wait.until(EC.element_to_be_clickable(self.locators.EMAIL_INPUT))
        email_field.clear()
        email_field.send_keys(email)
        return self

    def enter_password(self, password):
        password_field = self.wait.until(EC.element_to_be_clickable(self.locators.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)
        return self

    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.LOGIN_BUTTON)).click()
        return self

    def is_my_account_title_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.locators.MY_ACCOUNT_TITLE)).is_displayed()
        except:
            return False


