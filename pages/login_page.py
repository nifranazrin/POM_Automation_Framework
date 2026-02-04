from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import TestData

class LoginPage(BasePage):
    """
    Page Object for the Login Page.
    Contains locators and actions specific to the Login Page.
    """

    # 1. By Locators 
    _EMAIL_FIELD = (By.NAME, "username")
    _PASSWORD_FIELD = (By.NAME, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    #  Locator for the error message 
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "p.oxd-alert-content-text")

    # 2. Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # 3. Page Actions 
    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self._EMAIL_FIELD, username)
        self.do_send_keys(self._PASSWORD_FIELD, password)
        self.do_click(self._LOGIN_BUTTON)

    #  if login failed
    def is_login_failed(self):
        """Returns the text of the error message if displayed"""
        return self.get_element_text(self._ERROR_MESSAGE)