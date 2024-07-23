from selenium.webdriver.common.by import By


class Accountsuccesspage:
    def __init__(self, driver):
        self.driver = driver
        Account_creation_message = "//div[@id='content']/h1"
        

    def retrieve_account_creation_xpath(self):
       return self.driver.find_element(By.XPATH, self.Account_creation_message).text