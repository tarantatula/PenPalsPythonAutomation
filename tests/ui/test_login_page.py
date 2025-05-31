import time

import pytest
from selenium.webdriver.common.by import By

from pages.public_pages.login_page import LoginPage

pytestmark = pytest.mark.ui


@pytest.mark.usefixtures("driver")
class TestLoginPage:

    def setup_method(self, method):
        self.driver.get("http://localhost:44763/login.aspx")
        self.login_page = LoginPage(self.driver)
        self.login_page.wait_for_page_to_load()

    def test_1_login_fail(self):
        self.login_page.set_username("wrett")
        self.login_page.set_password("d123412")
        self.login_page.click_login()
        validation_error = self.login_page.get_validation_error()
        assert validation_error, f"Missing validation error! {validation_error}"

    def test_2_missing_username(self):
        self.login_page.set_username("")
        self.login_page.set_password("sdfgsdfgsdfgdsfg")
        self.login_page.click_login()
        self.login_page.wait_for_page_to_load()
        get_url = self.login_page.driver.current_url
        assert get_url == "http://localhost:44763/login.aspx", f"Incorrect url ({get_url}) are you logged in?"

    def test_3_login_success(self):
        self.login_page.set_username("tarantula2")
        self.login_page.set_password("12345")
        self.login_page.click_login()
        self.login_page.wait_for_element((By.ID, "cphMain_cphBody_btnAll"))
        get_url = self.login_page.driver.current_url
        assert get_url == "http://localhost:44763/pages/search.aspx", f"Incorrect url ({get_url}) are you logged in?"
