import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class TestLogin:
 def test_Login_with_valid_credential(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("Raghu20@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("Rag$1999")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_diplayed()

 def test_Login_without_entering_credential(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("Raghu20@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("Rag$1999")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        excepted_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            excepted_warning_message)
