import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeliveryAddress:
    def __init__(self, driver):
        self.driver = driver
        self.full_Name = "address-ui-widgets-enterAddressFullName"
        self.mobile = "address-ui-widgets-enterAddressPhoneNumber"
        self.pin_Code = "address-ui-widgets-enterAddressPostalCode"
        self.address = "address-ui-widgets-enterAddressLine1"
        self.area = "address-ui-widgets-enterAddressLine2"
        self.landmark = "address-ui-widgets-landmark"
        self.use_this_address_button = "// *[ @ id = 'address-ui-widgets-form-submit-button'] / span / input"

    def get_Full_Name(self):
        return self.driver.find_element(By.ID, self.full_Name)

    def get_Mobile(self):
        return self.driver.find_element(By.ID, self.mobile)

    def get_Pin_Code(self):
        return self.driver.find_element(By.ID, self.pin_Code)

    def get_Address(self):
        return self.driver.find_element(By.ID, self.address)

    def get_Area(self):
        return self.driver.find_element(By.ID, self.area)

    def get_Landmark(self):
        return self.driver.find_element(By.ID, self.landmark)

    def get_Use_this_address_button(self):
        return self.driver.find_element(By.XPATH, self.use_this_address_button)

    #######################

    def fill_address_details(self, full_name, mobile, pin_code, address, area, landmark):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('id', self.Full_Name)))
        time.sleep(7)
        self.get_Full_Name().send_keys(full_name)
        self.get_Mobile().send_keys(mobile)
        self.get_Pin_Code().send_keys(pin_code)
        self.get_Address().send_keys(address)
        self.get_Area().send_keys(area)
        self.get_Landmark().send_keys(landmark)
        time.sleep(5)

    def click_sign_in_button(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(('xpath', self.use_this_address_button)))
        self.get_Use_this_address_button().click()
        time.sleep(10)
