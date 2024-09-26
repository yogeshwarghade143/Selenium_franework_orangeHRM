from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

chromium_binary = 'chromium 117/c/chrome.exe'
options = webdriver.ChromeOptions()
options.binary_location = chromium_binary


driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options = options)

driver.get("https://pypi.org/project/webdriver-manager/")