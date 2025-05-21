import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class WelcomePage(BasePage):
    SEARCH_TEXTBOX = (By.CLASS_NAME, "search-textbox")
    SEARCH_BUTTON = (By.ID, "btnSearch")
    SEARCH_RESULTS = (By.CLASS_NAME, "recipe-content")

    def search_recipe(self, search_text):
        self.driver.find_element(*self.SEARCH_TEXTBOX).send_keys(search_text)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        self.wait_for_elements(self.SEARCH_RESULTS)
        time.sleep(1)

    def get_results_count(self):
        results = self.wait_for_elements(self.SEARCH_RESULTS)
        return len(results)

    def get_result(self):
        self.wait_for_elements(self.SEARCH_RESULTS)
        result = self.wait_for_element(self.SEARCH_RESULTS)
        return result

    def change_to_hebrew(self):
        self.driver.find_element(By.ID, "lsLanguage_lbHebrew").click()

    def change_to_english(self):
        self.driver.find_element(By.ID, "lsLanguage_lbEnglish").click()

    def get_main_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".mainview h1").text

    def get_first_recipe_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".recipe-details h3 span").text
