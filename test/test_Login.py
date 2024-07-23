from datetime import datetime
import pytest

from Utilities import Excelreader
from pageobjectmodel import Accountpage
from pageobjectmodel.Homepage import Homepage
from pageobjectmodel.Loginpage import Loginpage
from test.Basetest import Basetest


class TestLogin(Basetest):
    @pytest.mark.parametrize("email_address", "password",Excelreader.get_data_from_excel("Excelfiles/Tutorialsninj.xlsx","logintest"))

    def test_Login_with_valid_credentials(self, email_address,password ):
        home_page = Homepage(self.driver)
        Login_page = home_page.navigate_to_login_page()
        Account_page = Login_page.login_to_application("Raghu20@gmail.com","Rag$1999")
        assert Account_page.displayed_edit_your_account_information

    def test_login_with_invalid_email_and_password(self):
        home_page = Homepage(self.driver)
        Login_page = home_page.navigate_to_login_page()
        Login_page.login_to_application(self.generate_email_with_time_stamp(),"Rag$1999")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert Login_page.retrieve_warning_message().__contains__( expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = Homepage(self.driver)
        Login_page = home_page.navigate_to_login_page()
        Login_page.enter_email_address_filed("Raghu20@gmail.com")
        Login_page.enter_password_("1234")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert Login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credential(self):
        home_page = Homepage(self.driver)
        Login_page = home_page.navigate_to_login_page()
        Login_page.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert Login_page.retrieve_warning_message().__contains__(
                    expected_warning_message)




