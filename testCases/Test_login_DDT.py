import time
import pytest
from selenium import webdriver
from pageObject.loginPage import Login
from utilities import XLutils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator

class Test_002_login_DDT:
    baseUrl = ReadConfig.getApplicationURL()
    path = "E:\\software testing\\lectures\\selenium_framework\\testData\\Book1.xlsx"

    # creating logger object or variable and callling loggen() method from LogGen class
    logger = LogGenerator.loggen()

    def test_Login_DDT(self, setup):
        self.logger.info("**** verifying Test_002_login_DDT test ****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.loginObject = Login(self.driver)

        self.row=XLutils.getRowCount(self.path, "Sheet2")
        print("number of rows:", self.row)

        lst_status = []


        for i in range(2, self.row+1):
            self.username = XLutils.readData(self.path, "Sheet5", i, 1)      #to get username from rth row n 1st clmn  from xl sheet
            self.password = XLutils.readData(self.path, "Sheet5", i, 2)      #to get password from rth row n 2ndclmn  from xl sheet
            self.exp = XLutils.readData(self.path, "Sheet5", i, 3)           #to get exp result from rth row n 3rd clmn from xl sheet
            self.driver.implicitly_wait(10)
            self.loginObject.setUserName(self.username)
            self.loginObject.setPassword(self.password)
            time.sleep(5)
            self.loginObject.loginButton()
            time.sleep(5)

            print(f"userID : {self.username}  userpassword : {self.password} ")
            print(lst_status)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:                                          #if act_title=exp_title and exp value from XL sheet is (PASS) then test is successful else test is failed
                if self.exp=="pass":
                    self.logger.info("** test_Login_DDT is passed ")
                    self.loginObject.logoutButton()
                    lst_status.append("pass")
                    time.sleep(2)
                else:
                    self.logger.info("** test_Login_DDT is failed ")
                    self.loginObject.logoutButton()
                    lst_status.append("fail")
                    time.sleep(2)
            else:       #if act_title != exp_title and exp value from XL sheet is (FAIL) then test is successful else test is failed
                if self.exp == "pass":
                    self.logger.info("** test_Login_DDT is failed ")
                    lst_status.append("pass")
                    time.sleep(2)
                else:
                    self.logger.info("** test_Login_DDT is passed ")
                    lst_status.append("pass")
                    time.sleep(2)

        if "fail" not in lst_status:
            self.logger.info("** Test_001_login_DDT is passed **")
            self.driver.close()
            assert True

        else:
            self.logger.info("** Test_001_login_DDT is failed **")
            assert False









