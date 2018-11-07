from selenium import webdriver
import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils import utils as constants

@pytest.mark.usefixtures("test_setup")
class Test_Login():


    def test_login(self):
        driver = self.driver
        driver.get(constants.Vison_URL)
        login = LoginPage(driver)
        login.enter_loginId(constants.Login_Id)
        login.enter_password(constants.Password)
        login.click_loginButton()

    def verify_items_displayed(self):
        driver = self.driver
        homepage =HomePage(driver)
        homepage.home_list_isDisplayed()
        homepage.transferPayment_list_isDisplayed()
        homepage.transferPayment_list_isDisplayed()
        homepage.billPay_list_isDisplayed()
        homepage.expressDeposit_list_isDisplayed()
        homepage.commercial_list_istDisplayed()
        homepage.cardSwap_list_isDisplayed()
        homepage.eStatements_list_isDisplayed()
        homepage.liveChat_list_isDisplayed()
        homepage.applyForALoan_list_isDisplayed()
        homepage.services_lsit_isDisplayed()
        homepage.messages_lsit_isDisplayed()
        homepage.settings_list_isDisplayed()
        homepage.logOut_list_isDisplayed()

    def test_logout(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.logOut_list_isDisplayed()
        homepage.clickLogout()

