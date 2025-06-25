from selenium.webdriver.common.by import By

class HomeElements:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self):
        return self.driver.find_element(By.NAME, "search")


