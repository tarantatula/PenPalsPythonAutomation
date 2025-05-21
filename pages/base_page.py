from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class BasePage:
    SEARCH_RESULTS = (By.CLASS_NAME, "recipe-content")
    LOGO_BUTTON = (By.CSS_SELECTOR, "header h1 a")
    LANGUAGE_BUTTON = (By.ID, "earth-button")
    LANGUAGE_ITEM = (By.CLASS_NAME, "language-item")
    LANGUAGE_LIST = (By.ID, "language-list")

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator):
        waited_element = self.wait.until(EC.presence_of_element_located(locator))
        return waited_element

    def wait_for_elements(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_logo(self):
        self.driver.find_element(*self.LOGO_BUTTON).click()

    def click_change_language(self):
        language_button = self.driver.find_element(*self.LANGUAGE_BUTTON)
        language_button.click()
        sleep(0.5)
        language_list = self.driver.find_element(*self.LANGUAGE_LIST)
        return language_list.size

    # run after redirection
    def wait_for_page_to_load(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
