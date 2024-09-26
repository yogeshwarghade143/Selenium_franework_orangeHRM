import pytest
from selenium import webdriver
from pageObject.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator


class Test_001_login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getpassword()
    # creating logger object or variable and callling loggen() method from LogGen class
    logger = LogGenerator.loggen()

    def test_Homepage_Title(self, setup):
        self.logger.info("**** Test_001_login ****")
        self.logger.info("**** verifying homepage title ****")
        self.driver = setup
        self.logger.info("open url")
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.logger.info("****  homepage title page is verified  ****")
        else:
            self.driver.get_screenshot_as_file(
                'E:\\software testing\\lectures\\selenium_framework\\screenshots\\test_Homepage_Title.png')
            self.driver.close()
            self.logger.info("****  homepage title page is failed  ****")

            assert False

    def test_Login(self, setup):
        self.logger.info("**** verifying login test ****")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginObject = Login(self.driver)
        self.loginObject.setUserName(self.username)
        self.loginObject.setPassword(self.password)
        self.loginObject.loginButton()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":

            assert True
            self.logger.info("**** login page title is passed  ****")

        else:
            self.driver.get_screenshot_as_file(
                'E:\\software testing\\lectures\\selenium_framework\\screenshots\\test_Login.png')

            self.logger.info("**** login page title is failed  ****")
            assert False
        self.driver.close()
