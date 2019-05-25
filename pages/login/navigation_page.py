import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _post = "//a[@title='Posts']"
    _reports = "//a[@title='Reports']//span[1]"
    _people = "//a[@title='People']"
    _drawing = "//a[@title='Drawings']//span[1]"
    _insights = "//a[@title='Insights']//span[1]"
    _user_settings_icon = "//div[@class='column small-6 ng-scope']//img[@class='radius']"


    def navigateToPost(self):
        self.elementClick(locator=self._post, locatorType="xpath")

    def navigateToReports(self):
        self.elementClick(locator=self._reports, locatorType="xpath")

    def navigateToPeople(self):
        self.elementClick(locator=self._people, locatorType="xpath")

    def navigateToDrawing(self):
        self.elementClick(locator=self._drawing, locatorType="xpath")

    def navigateToInsights(self):
        self.elementClick(locator=self._insights, locatorType="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                      locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon,
                                      locatorType="xpath")