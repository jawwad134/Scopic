import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResults:
    def __init__(self, driver):
        self.driver = driver
        self.search_item = "(//span[contains(text(),'Villain Perfume For Men 100 Ml - Eau De Parfum - P')])"
        self.add_to_cart = "add-to-cart-button"
        self.proceed_to_buy = "proceedToRetailCheckout"

    def switch_window_tab(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                return self.driver.switch_to.window(window_handle)


    def get_Search_item(self):
        return self.driver.find_element(By.XPATH, self.search_item)

    def click_Search_item(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('xpath', self.search_item)))
        self.get_Search_item().click()

    def get_add_to_cart(self):
        return self.driver.find_element(By.ID, self.add_to_cart)

    def click_add_to_cart(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('id', self.add_to_cart)))
        time.sleep(7)
        self.get_add_to_cart().click()

    def get_proceed_to_buy(self):
        return self.driver.find_element(By.NAME, self.proceed_to_buy)

    def click_proceed_to_buy(self):
        time.sleep(7)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('id', self.proceed_to_buy)))
        self.get_proceed_to_buy().click()
