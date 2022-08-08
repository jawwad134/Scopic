import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.Search_bar = "twotabsearchtextbox"
        self.Search_btn = "nav-search-submit-button"


    def get_Search_bar(self):
        return self.driver.find_element(By.ID, self.Search_bar)

    def get_Search_btn(self):
        return self.driver.find_element(By.ID, self.Search_btn)

    def enter_text_Search_bar(self, Search_bar):
        self.get_Search_bar().send_keys(Search_bar)

    def click_search_button(self):
        self.get_Search_btn().click()


