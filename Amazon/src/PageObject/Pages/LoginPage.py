import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"

# base_url = "https://www.amazon.in"

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = "(//span[@class='nav-action-inner'][normalize-space()='Sign in'])[2]"
        self.email = "ap_email"
        self.continue_button = "continue"
        self.password = "ap_password"
        self.sign_in_submit = "signInSubmit"
        self.LoginPage_verification="nav-link-accountList-nav-line-"

    def get_sign_in_button(self):
        return self.driver.find_element(By.XPATH, self.sign_in_button)

    def get_email(self):
        return self.driver.find_element(By.ID, self.email)

    def get_continue_button(self):
        return self.driver.find_element(By.ID, self.continue_button)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_sign_in_submit(self):
        return self.driver.find_element(By.ID, self.sign_in_submit)

    def get_LoginPage_verification(self):
        return self.driver.find_element(By.ID, self.LoginPage_verification)


    def click_sign_in_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('xpath', self.sign_in_button)))
        self.get_sign_in_button().click()

    def sign_in(self, email):
        # self.switch_to_iframe()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('id', self.email)))
        self.get_email().send_keys(email)

    def sign_password(self, password):
        # self.switch_to_iframe()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('id', self.password)))
        self.get_password().send_keys(password)

    def click_continue_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('id', self.continue_button)))
        self.get_continue_button().click()

    def click_sign_in_submit(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('id', self.sign_in_submit)))
        self.get_sign_in_submit().click()

    def LoginPage_verification(self):
        self.get_LoginPage_verification().is_displayed()

    @staticmethod
    def get_base_url():
        return base_url
