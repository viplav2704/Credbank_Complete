import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# def pytest_addoptions(parser):
#     parser.addoption("--browser")

url_main_page = 'https://bankapp.credence.in'
url_login = "https://bankapp.credence.in/login.html"


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_main_page)
    yield driver
    driver.quit()  # teardown process


@pytest.fixture(scope="class")
def setup_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_login)
    yield driver
    driver.quit()
