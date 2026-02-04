import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.config import TestData

@pytest.fixture(scope="class")
def init_driver(request):
    """
    This fixture initializes the driver before the test class starts
    and quits the driver after the test class ends.
    """
    print("------ Setup: Launching Browser ------")
    
    
    service = Service(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service)
    
    web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL) 
    
    request.cls.driver = web_driver 
    
    yield 
    
    print("------ Teardown: Closing Browser ------")
    web_driver.quit()