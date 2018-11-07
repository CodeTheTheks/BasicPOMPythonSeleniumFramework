from Locators.commonLocators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver

class HomePage(object):
    def __init__(self, driver):
        self.driver = driver

        self.home_list_xpath = driver.find_element(By.XPATH, Locators.home)
        self.transferPayment_list_xpath = driver.find_element(By.XPATH, Locators.transferPayment)
        self.billPay_list_xpath = driver.find_element(By.XPATH, Locators.billPay)
        self.expressDeposit_list_xpath = driver.find_element(By.XPATH, Locators.expressDeposit)
        self.commercial_list_xpath = driver.find_element(By.XPATH, Locators.commercial)
        self.cardSwap_list_xpath = driver.find_element(By.XPATH, Locators.cardSwap)
        self.eStatements_list_xpath = driver.find_element(By.XPATH, Locators.eStatements)
        self.liveChat_list_xpath = driver.find_element(By.XPATH, Locators.liveChat)
        self.applyForALoan_list_xpath = driver.find_element(By.XPATH, Locators.applyForALoan)
        self.services_list_xpath = driver.find_element(By.XPATH, Locators.services)
        self.messages_list_xpath = driver.find_element(By.XPATH, Locators.messages)
        self.settings_list_xpath = driver.find_element(By.XPATH, Locators.settings)
        self.logOut_list_xpath = driver.find_element(By.XPATH, Locators.logOut)

    def home_list_isDisplayed(self):
       if self.home_list_xpath.is_displayed():
           print ("Home is displayed")
       else:
           print ("Home is not diplayed on Home page")

    def transferPayment_list_isDisplayed(self):
        if self.transferPayment_list_xpath.is_displayed():
            print("Transfer/Payment is displayed on Home page")
        else:
            print("Transfer/Payment is not displayed on Home page")

    def billPay_list_isDisplayed(self):
        if self.billPay_list_xpath.is_displayed():
            print("Bill Pay is displayed on Home Page")
        else:
            print("Bill Pay is displayed not on Home Page")

    def expressDeposit_list_isDisplayed(self):
        if self.expressDeposit_list_xpath.is_displayed():
            print("Express Deposit is displayed on Home Page")
        else:
            print("Express Deposit is not displayed on Home Page")

    def commercial_list_istDisplayed(self):
        if self.commercial_list_xpath.is_displayed():
            print("Commercial is diplayed on Home Page")
        else:
            print("Commercial is diplayed on Home Page")

    def cardSwap_list_isDisplayed(self):
        if self.cardSwap_list_xpath.is_displayed():
            print("Card Swap is displayed on Home Page")
        else:
            print("Card Swap is not displayed on Home Page")

    def eStatements_list_isDisplayed(self):
        if self.eStatements_list_xpath.is_displayed():
            print("EStatements is displayed on Home Page")
        else:
            print("EStatements is not displayed on Home Page")

    def liveChat_list_isDisplayed(self):
        if self.liveChat_list_xpath.is_displayed():
            print("Live Chat is displayed on Home Page")
        else:
            print("Live Chat is not displayed on Home Page")

    def applyForALoan_list_isDisplayed(self):
        if self.applyForALoan_list_xpath.is_displayed():
            print("Apply for a Loan is displayed on Home Page")
        else:
            print("Apply for a Loan is displayed on Home Page")

    def services_lsit_isDisplayed(self):
        if self.services_list_xpath.is_displayed():
            print("Services is displayed on Home page")
        else:
            print("Services is not displayed on Home page")

    def messages_lsit_isDisplayed(self):
        if self.messages_list_xpath.is_displayed():
            print("Messages is displayed on Home Page")
        else:
            print("Messages is displayed on Home Page")

    def settings_list_isDisplayed(self):
        if self.services_list_xpath.is_displayed():
            print("Setting is displayed on Home Page")
        else:
            print("Settings is not didplayed on Home Page")

    def logOut_list_isDisplayed(self):
        if self.logOut_list_xpath.is_displayed():
            print("Logout is displayed on Home page")
        else:
            print("Logout is displayed on Home page")

    def clickLogout(self):
        self.logOut_list_xpath.click()



