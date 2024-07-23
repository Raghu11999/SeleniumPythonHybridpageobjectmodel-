from selenium.webdriver.common.by import By


class Accountpage:
    def __init__(self,driver):
        self.driver = driver
        edit_your_account_information_link_text = "Edit your account information"

    def displayed_edit_your_account_information(self):
        return self.driver.find_element(By.XPATH, self.edit_your_account_information_link_text).is_displayed()

