import utilities.custom_logger as cl
from pages.login.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "//input[@id='login-email']"
    _password_field = "//input[@id='password']"
    _login_button = "//button[@type='submit']"

    #def clickLoginLink(self):
       # self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        #self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement("//div[@class='column small-6 ng-scope']//img[@class='radius']",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//div[@class='column small-6 ng-scope']//img[@class='radius']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//div[contains(text(),'Your email address or password is invalid.')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Fieldlens - Sign in to your FieldLens account")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//div[@class='ui-select--drop-down-container']//li[5]",
                          locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//div[@class='ui-select--drop-down-container']//li[5]",
                          locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field, locatorType="xpath")
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field, locatorType="xpath")
        passwordField.clear()
