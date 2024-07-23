import pytest
from selenium.webdriver.common.by import By

from pageobjectmodel.Homepage import Homepage
from pageobjectmodel.searchpage import searchpage
from test.Basetest import Basetest


class TestSearch(Basetest):
    def test_search_for_a_valid_product(self):
        home_page = Homepage(self.driver)
        search_page = home_page.search_for_a_product("Hp")

        assert search_page.display_status_of_valid_product()

    def test_search_for_an_invalid_products(self):
        home_page = Homepage(self.driver)
        search_page = home_page.search_for_a_product("Honda")
        expected_text = "there is no product that matches the search criteria"
        assert search_page.retrieve_no_product_message().__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        home_page = Homepage(self.driver)
        search_page = home_page.search_for_a_product("Honda")

        expected_text = "there is no product that matches the search criteria"
        assert search_page.retrieve_no_product_message().__eq__(expected_text)





