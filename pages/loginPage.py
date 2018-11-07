from Locators.commonLocators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.loginId_textbox_id = driver.find_element(By.ID, Locators.userId)
        self.password_textbox_id = driver.find_element(By.ID, Locators.password)
        self.loginButton_button_xpath = driver.find_element(By.XPATH, Locators.loginButton)

    def enter_loginId(self, loginId):
        self.loginId_textbox_id.clear()
        self.loginId_textbox_id.send_keys(loginId)

    def enter_password(self, password):
        self.password_textbox_id.clear()
        self.password_textbox_id.send_keys(password)

    def click_loginButton(self):
        self.loginButton_button_xpath.click()





