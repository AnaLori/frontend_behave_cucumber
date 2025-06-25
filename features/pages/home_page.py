from features.elements.home_elements import HomeElements

class HomePage:
    def __init__(self, driver):
        self.elements = HomeElements(driver)

    def search_input_is_visible(self):
        return self.elements.search_input().is_displayed()


