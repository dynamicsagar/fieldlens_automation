import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class globalTest(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators:
    _projectSelect = "//span[contains(text(),'arctest')]"
    _unread_icon = "//span[@class='unread-count ng-binding']"
    _unread_activity = "//*[@class='fl-action-icon unread']"
    _check_textpresent = "//span[contains(text(),'Manage activity for')]"

    def selectProject(self):
        self.waitForElement(self._projectSelect, locatorType="xpath")
        self.elementClick(self._projectSelect, locatorType="xpath")

    def clickUnreadIcon(self):
        self.waitForElement(self._unread_icon, locatorType="xpath")
        self.elementClick(self._unread_icon, locatorType="xpath")

    def clickUnreadAct(self):
        self.elementClick(self._unread_activity, locatorType="xpath")

    def activityUnread(self):
        self.selectProject()
        time.sleep(2)
        self.clickUnreadIcon()
        time.sleep(0.5)
        self.clickUnreadAct()

    def verifyUnreadActivityText(self):
        result = self.isElementPresent(self._check_textpresent, locatorType="xpath")
        return result


