from re import search

import Basepage
from selenium.webdriver.common.by import By


from pageobjectmodel.Loginpage import Loginpage
from pageobjectmodel.Registerpage import Registerpage
from pageobjectmodel.searchpage import searchpage


class Homepage(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

        search_box_field_Name = "search"
        search_button_xpath = "//button[contains(@class,'btn-default')]"
        my_account_drop_menu = "//span[text()='My Account']"
        login_option_link_text = "Login"
        Register_option_link_text = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name,self.search_box_field_Name)


    def click_on_search_button(self):
        self.element_click(self.search_button_xpath)
        return search(self.driver)

    def click_on_my_account_drop_menu(self):
        self.element_click(self.my_account_drop_menu)

    def select_login_option(self):
        self.element_click(self.login_option_link_text)
        return Loginpage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.Register_option_link_text).click()
        return Registerpage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()

    def search_for_a_product(self,product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()


