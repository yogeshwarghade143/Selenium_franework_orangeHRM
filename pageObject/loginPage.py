from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    link_logout_xpath = '/html/body/div[3]/nav/div/ul/li[3]/a'


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def loginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logoutButton(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

