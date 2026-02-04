import pytest
from pages.login_page import LoginPage
from config.config import TestData

@pytest.mark.usefixtures("init_driver")
class TestLogin:
    
    def test_login_page_title(self):
        """
        Test Case 1: Verify the login page title is correct.
        """
        print("--- Running Test: Check Title ---")
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_invalid_login(self):
        """
        Test Case 2 (Negative): Verify that invalid login shows an error.
        """
        print("--- Running Test: Invalid Login ---")
        self.loginPage = LoginPage(self.driver)
        
        #  login with WRONG password
        self.loginPage.do_login(TestData.USERNAME, "WrongPassword")
        
        # Verify the error message contains 'Invalid credentials'
        assert "Invalid credentials" in self.loginPage.is_login_failed()

    def test_login(self):
        """
        Test Case 3: Verify the user can login with valid credentials.
        """
        print("--- Running Test: Valid Login ---")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)