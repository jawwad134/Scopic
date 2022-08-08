import time

from src.PageObject.Pages import LoginPage

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.LoginPage import LoginPage
from src.PageObject.Pages.HomePage import HomePage
from src.PageObject.Pages.SearchResults import SearchResults
from src.PageObject.Pages.DeliveryAddress import DeliveryAddress

class Test_AmazonLoginTest(WebDriverSetup):

    def test_complete_end_to_end_flow(self):

        driver = self.driver
        self.driver.get(LoginPage.get_base_url())

        # Creating object for LoginPage and using the Login Functions
        login_page = LoginPage(driver)
        login_page.sign_in("test@testemail.com")
        login_page.click_continue_button()
        login_page.sign_password("Password")
        login_page.click_sign_in_submit()

        # Creating object for HomePage and using the HomePage Functions and searching the desired item
        home_page = HomePage(driver)
        home_page.enter_text_Search_bar("men perfumes")
        home_page.click_search_button()


        # Creating object for SearchPage and using the SearchPage Functions
        # Switching windows tab -  adding item to cart - proceed to buy
        search_results = SearchResults(driver)
        search_results.click_Search_item()
        search_results.switch_window_tab()
        search_results.click_add_to_cart()
        search_results.click_proceed_to_buy()

        # Creating object for Delivery Address and using the Function with required data parameters and form filling
        delivery_address = DeliveryAddress(driver)
        delivery_address.fill_address_details("Jawwad Sadiq",
                                              "987654321011",
                                              "400004",
                                              "Lal Bahadur Shastri Rd",
                                              "Amrut Nagar",
                                              "Ghatkopar West")
        delivery_address.click_sign_in_button()


