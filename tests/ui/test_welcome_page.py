import time

import pytest
from selenium.webdriver.common.by import By

from pages.public_pages.welcome_page import WelcomePage
from pages.public_pages.signup_page import SignupPage
from pages.public_pages.login_page import LoginPage

pytestmark = pytest.mark.ui


@pytest.mark.usefixtures("driver")
class TestWelcomePage:

    def setup_method(self, method):
        self.driver.get("http://localhost:44763")
        self.welcome_page = WelcomePage(self.driver)
        self.welcome_page.wait_for_page_to_load()

    def test_1_search_for_cream(self, driver):
        self.welcome_page.search_recipe("cream")
        result_count = self.welcome_page.get_results_count()
        assert result_count == 1, f"Expected 1 result but found {result_count} results"

    def test_2_logo_click(self, driver):
        self.welcome_page.click_logo()
        self.welcome_page.wait_for_page_to_load()
        assert self.welcome_page.get_results_count() > 1, "Expected multiple results after logo click"

    def test_3_language_element(self, driver):
        language_size1 = self.welcome_page.click_change_language()
        assert language_size1['width'] == 170, f"not expanded {language_size1}"
        language_size2 = self.welcome_page.click_change_language()
        assert language_size2['width'] != 170, f"expanded {language_size2}"

    def test_4_change_language(self, driver):
        self.welcome_page.click_change_language()
        self.welcome_page.change_to_hebrew()
        self.welcome_page.search_recipe("cream")
        main_title = self.welcome_page.get_main_title()
        assert main_title == "ברוכים הבאים ל-PANPALS!", f"Unexpected title {main_title}"
        recipe_title = self.welcome_page.get_first_recipe_title()
        assert recipe_title == "פטיט-בור קרם עוגה קרה", f"Unexpected title {recipe_title}"

    def test_5_signup_page(self, driver):
        self.welcome_page.navigate_to_signup()
        signup_page = SignupPage(self.driver)
        signup_page.wait_for_element((By.ID, "cphMain_txtUsername"))
        page_title = signup_page.get_page_title()
        assert page_title == "Pan Pals - Sign Up", f"Page title is incorrect ({page_title})." \
                                                 f" Are you navigated to the correct page?"

    def test_6_login_page(self, driver):
        self.welcome_page.click_logo()
        self.welcome_page.navigate_to_login()
        login_page = LoginPage(self.driver)
        login_page.wait_for_element((By.ID, "cphMain_btnSignUp"))
        page_title = login_page.get_page_title()
        assert page_title == "Pan Pals - Login", f"Page title is incorrect ({page_title})." \
                                                 f" Are you navigated to the correct page?"
