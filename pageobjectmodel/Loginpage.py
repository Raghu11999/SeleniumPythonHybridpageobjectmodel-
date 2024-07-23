from selenium.webdriver.common.by import By

from pageobjectmodel.Accountpage import Accountpage


class Loginpage:
    def __init__(self,driver):
        self.driver = driver

        email_address_field_id = "input-email"
        password_field_id = "input-password"
        Login_button_xpath = "//input[@value='Login']"
        warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address_filed(self,email_address_text):
        self.driver.find_element(By.ID, self.enter_email_address_field).click()
        self.driver.find_element(By.ID, self.enter_email_address_field).clear()
        self.driver.find_element(By.ID, self.enter_email_address_field).send_key(email_address_text)

    def enter_password_(self,password_field_id):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_key(password_field_id)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.Login_button_xpath)
        return Accountpage(self.driver)

    def login_to_application(self,email_address_text,password_field_id):
        self.enter_email_address_filed(email_address_text)
        self.enter_password_(password_field_id)
        return self.click_on_login_button()

    def retrieve_warning_message(self):
         return self.driver.find_element(By.XPATH, self.warning_message_xpath).text





