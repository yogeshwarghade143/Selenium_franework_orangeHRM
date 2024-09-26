import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

    return driver
#
# from selenium import webdriver
# import pytest
#
#
# @pytest.fixture()
# def setup(browser):
#     driver = webdriver.Chrome()
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#     elif browser == 'edge':
#         driver = webdriver.Edge()
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#     return driver
#
#
# def pytest_addoption(parser):  # this will get the value from cli  (command line interface) i.e. terminal
#     parser.addoption("--browser")
#
#
# @pytest.fixture()  # this will give browser value to set up the value which we will put in terminal
# def browser(request):
#     return request.config.getoption("--browser")
