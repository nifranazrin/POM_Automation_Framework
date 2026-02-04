class TestData:
    # 1. The URL we are testing (A safe demo site)
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # 2. The Credentials (In a real job, these are hidden in env variables)
    USERNAME = "Admin"
    PASSWORD = "admin123"

    # 3. Expected Results (For assertions)
    LOGIN_PAGE_TITLE = "OrangeHRM"