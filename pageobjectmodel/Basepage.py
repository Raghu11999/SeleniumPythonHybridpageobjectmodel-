from selenium.webdriver.common.by import By


class Basepage:
    def __init__(self,driver):
        self.driver = driver

    def type_into_element(self,text,locator):
        element = self.get_element(locator)
        element.click()
        element.clear()
        element.send_keys()

    def element_click(self,locator):
        element = self.get_element(locator)
        element.click()


    def get_element(self,locator):
        element = None
        if locator.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator)
            elif locator.__contains__("_name"):
                self.driver.find_element(By.NAME, locator)
            elif locator.__contains__("_class_name"):
                 self.driver.find_element(By.CLASS_NAME, locator)
            elif locator.__contains__("_link_text"):
             self.driver.find_element(By.LINK_TEXT, locator)
            elif locator.__contains__("-xpath"):
                self.driver(By.XPATH, locator)
            elif locator.__contains__("_css"):
                self.driver(By.CSS_SELECTOR, locator)
            return element






