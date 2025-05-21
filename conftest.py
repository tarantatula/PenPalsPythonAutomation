import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver  # bind to test class
    yield driver
    driver.quit()
