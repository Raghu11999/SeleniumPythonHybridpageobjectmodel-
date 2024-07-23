from selenium.webdriver.common.by import By

from pageobjectmodel.Accountsuccesspage import Accountsuccesspage


class Registerpage:
    def __init__(self,driver):
        self.driver = driver

        first_name_field_id = "input-firstname"
        last_name_field_id = "input-lastname"
        email_field_id = "input-email"
        telephone_filed_id = "input-telephone"
        password_field_id = "input-password"
        confirm_password_field_id = "input-confirm"
        agree_filed_name = "agree"
        continue_button_xpath = "//input[@value='Continue']"
        yes_radio_button = "//input[@name='newsletter'][@value=1]"
        duplicate_email_Waring_message_xpath = "//div[@id='account-register']/div[1]"
        privacy_policy_waring_xpath = "//div[@id='account-register']/div[1]"
        first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div[1]"
        last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div[1]"
        Email_warning_xpath = "//input[@id='input-email']/following-sibling::div[1]"
        telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div[1]"
        password_warning_xpath = "//input[@id='input-password']/following-sibling::div[1]"

    def enter_first_name(self,first_name_text):
        self.driver.find_element(By.ID, self.first_name_field_id).click()
        self.driver.find_element(By.ID, self.first_name_field_id).clear()
        self.driver.find_element(By.ID, self.first_name_field_id).send_key(first_name_text)

    def enter_last_name(self,last_name_text):
        self.driver.find_element(By.ID, self.last_name_field_id).click()
        self.driver.find_element(By.ID, self.last_name_field_id).clear()
        self.driver.find_element(By.ID, self.last_name_field_id).send_key(last_name_text)

    def enter_email(self,email_text):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_name_field_id).clear()
        self.driver.find_element(By.ID, self.email_name_field_id).send_key(email_text)

    def enter_telephone(self,telephone_text):
        self.driver.find_element(By.ID, self.telephone_filed_id).click()
        self.driver.find_element(By.ID, self.telephone_filed_id).clear()
        self.driver.find_element(By.ID, self.telephone_filed_id).send_key(telephone_text)

    def enter_password(self,password_text):
        self.driver.find_element(By.ID, self.password_filed_id).click()
        self.driver.find_element(By.ID, self.password_filed_id).clear()
        self.driver.find_element(By.ID, self.password_filed_id).send_key(password_text)

    def enter_confirm_password(self,confirm_password_text):
        self.driver.find_element(By.ID, self.confirm_password_filed_id).click()
        self.driver.find_element(By.ID, self.confirm_password_filed_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_filed_id).send_key(confirm_password_text)

    def select_agree_checkbox_field(self):
        self.driver.find_element(By.NAME, self.agree_filed_name).click()

    def continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return Accountsuccesspage(self.driver)

    def select_radio_button(self):
        self.driver.find_element(By.XPATH, self.select_radio_button).click()

    def Register_with_account(self,first_name_text,last_name_text,email_text,telephone_text,password_text, confirm_password_text,yes_or_no,privacy_policy):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.enter_confirm_password(confirm_password_text)
        if yes_or_no.__eq__("yes"):
            self.select_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
            return self.continue_button()

    def retrieve_duplicate_waring_message_text(self):
     return self.driver.find_element(By.XPATH, self.duplicate_email_Waring_message_xpath).text

    def retrieve_privacy_policy_warning(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_waring_xpath).text

    def retrieve_first_name_warning(self):
        return self.driver.find_element(By.XPATH, self.first_name_warning_xpath).text

    def retrieve_last_name_warning(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text

    def retrieve_email_warning(self):
        return self.driver.find_element(By.XPATH, self.Email_warning_xpath).text

    def retrieve_telephone_warning(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning_xpath).text

    def retrieve_password_warning(self):
        return self.driver.find_element(By.XPATH, self. password_warning_xpath).text

    def verify_all_warns(self, expected_privacy_policy_warning, expected_first_name_warning_message, expected_last_name_warning_message , expected_email_warning_message, expected_Telephone_warning_message, expected_password_warning_message):
        actual_privacy_policy_warning = self.retrieve_privacy_policy_warning()
        actual_first_name_warning_message = self.retrieve_first_name_warning()
        actual_last_name_warning_message = self.retrieve_last_name_warning()
        actual_email_warning_message = self.retrieve_email_warning()
        actual_telephone_warning_message = self.retrieve_telephone_warning()
        actual_password_warning_message = self.retrieve_password_warning()

        status = False

        if expected_privacy_policy_warning.__contains__(actual_privacy_policy_warning):
           if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
               if expected_last_name_warning_message.__eq__(actual_last_name_warning_message):
                   if expected_email_warning_message.__eq__(actual_email_warning_message):
                       if expected_Telephone_warning_message.__eq__(actual_telephone_warning_message):
                           if expected_password_warning_message(actual_password_warning_message):
                               status = True

                               return status



