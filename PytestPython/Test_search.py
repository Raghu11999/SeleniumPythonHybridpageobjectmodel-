
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common import by
@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
@allure.severity(allure.severity_level.NORMAL)
class TestSearch:
 def test_search_for_a_valid_product(self):
   self.driver.find_element(by.By.NAME,"search").send_keys("hp")
   self.driver.find_element(by.By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
   assert self. driver.find_element(by.By.LINK_TEXT,"HP LP3065").is_displayed()

 def test_search_for_a_invalid_product(self):
    self.driver.find_element(by.By.NAME, "search").send_keys("Honda")
    self.driver.find_element(by.By.XPATH, "//button[contains(@class,'btn btn-default btn-lg')]").click()
    expected_text="There is no product that matches the search criteria."
    assert self.driver.find_element(by.By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

 def test_search_without_providing_any_product(self):
   self.driver.find_element(by.By.NAME, "search").send_keys("")
   self.driver.find_element(by.By.XPATH, "//button[contains(@class,'btn btn-default btn-lg')]").click()
   expected_text = "There is no product that matches the search criteria."




