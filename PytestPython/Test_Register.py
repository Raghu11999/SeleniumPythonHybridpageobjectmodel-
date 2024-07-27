import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class TestRegister:
 def test_create_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Raghu")
        self.driver.find_element(By.ID,"input-lastname").send_keys("sk")
        self.driver.find_element(By.ID,"input-email").send_keys("Raghu2@gmail.com")
        self.driver.find_element(By.ID,"input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID,"input-password").send_keys("Rag$1999")
        self.driver.find_element(By.ID,"input-confirm").send_keys("Rag$1999")
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        excepected_text="Your Account Has Been Created !"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__contains__(excepected_text)

 def test_create_account_by_providing_fields(self):

                self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
                self.driver.find_element(By.LINK_TEXT, "Register").click()
                self.driver.find_element(By.ID, "input-firstname").send_keys("Raghu")
                self.driver.find_element(By.ID, "input-lastname").send_keys("sk")
                self.driver.find_element(By.ID, "input-email").send_keys("Raghu2@gmail.com")
                self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
                self.driver.find_element(By.ID, "input-password").send_keys("Rag$1999")
                self.driver.find_element(By.ID, "input-confirm").send_keys("Rag$1999")
                self.driver.find_element(By.XPATH,"//input[@value='1'][@name='newsletter']").click()
                self.driver.find_element(By.NAME, "agree").click()
                self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
                excepected_text = "Your Account Has Been Created !"
                assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(excepected_text)















