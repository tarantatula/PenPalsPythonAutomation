from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SignupPage(BasePage):

    def get_page_title_fake(self):
        return self.driver.title
