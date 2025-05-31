from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    def set_username(self, text):
        input_username = self.driver.find_element(By.ID, "cphMain_txtUsername")
        input_username.send_keys(text)

    def set_password(self, text):
        input_password = self.driver.find_element(By.ID, "cphMain_txtPassword")
        input_password.send_keys(text)

    def click_login(self):
        button_login = self.driver.find_element(By.ID,"cphMain_btnLogin")
        button_login.click()

    def get_validation_error(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "cphMain_lblNotAuthenticated"))).text
