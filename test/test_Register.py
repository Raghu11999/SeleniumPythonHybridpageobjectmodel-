from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from Utilities import Excelreader
from pageobjectmodel import Accountsuccesspage
from pageobjectmodel.Homepage import Homepage
from pageobjectmodel.Registerpage import Registerpage
from test.Basetest import Basetest


class TestRegister(Basetest):

    def register_with_mandatory_fields(self):
        home_page = Homepage(self.driver)
        Register_page = home_page.navigate_to_register_page()
        Account_success_page= Register_page.Register_with_account(Excelreader.get_cell_data("excelfiles/Tutorialsninj.xlsx","Registertest",2,1),
        Excelreader.get_cell_data("excelfiles/Tutorialsninj.xlsx", "Registertest",2,1),"Raghu", "sk",self.generate_email_with_time_stamp(),"1234567890","12345", "12345","no","select")
        Expected_account_message = "Your Account Has Been Created!"
        assert Account_success_page.retrieve_account_creation_xpath.__eq__(Expected_account_message)

    def test_register_with_all_fields(self):
        home_page = Homepage(self.driver)
        Register_page = home_page.navigate_to_register_page()
        Account_success_page = Register_page.Register_with_account("Raghu", "sk", self.generate_email_with_time_stamp(),"1234567890", "12345","12345","yes","select" )
        Expected_account_message = "Your Account Has Been Created!"
        assert Account_success_page.retrieve_account_creation_xpath.__eq__(Expected_account_message)

    def test_register_with_duplicate_email(self):
        home_page = Homepage(self.driver)
        Register_page = home_page.navigate_to_register_page()
        Register_page = Register_page.Register_with_account("Raghu","sk", "Raghu1@gmail.com", "1234567890","12345","12345","yes","select")


        Register_page.enter_first_name("Raghu")
        Register_page.enter_last_name("sk")
        Register_page.enter_email("Raghu1@gmail.com")
        Register_page.enter_telephone("1234567890")
        Register_page.enter_password("12345")
        Register_page.enter_confirm_password("12345")
        Register_page.select_radio_button()
        Register_page.select_agree_checkbox_field()
        Register_page.continue_button()
        Expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert Register_page.retrieve_duplicate_waring_message_text().__contains__(Expected_warning_message)

    def test_register_without_any_field(self):
        home_page = Homepage(self.driver)
        Register_page = home_page.navigate_to_register_page()
        Register_page = Register_page.Register_with_account("", "", "", "", "", "","no","no")
        assert Register_page.verify_all_warns()

