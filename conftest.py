import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)

    yield driver
    driver.quit()


# Constants
@pytest.fixture(scope="session")
def config():
    return {
        "LOGIN_URL": "https://magento.softwaretestingboard.com/customer/account/login",
        "ACCOUNT_URL": "https://magento.softwaretestingboard.com/customer/account/",
        "EMAIL": "lusine.testavetisyan_1@gmail.com",
        "PASSWORD": "Alina!2018",
        "NEW_PASSWORD": "Alina!2018",
    }




