from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    This class wraps Selenium commands. 
    It uses EXPLICIT WAITS to ensure the browser is ready before clicking.
    """

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        """Waits for element to be visible, then clicks."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """Waits for element to be visible, then types text."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        """Waits for element to be visible, then returns its text."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title):
        """Waits for the page title to match the given title."""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title