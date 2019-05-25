import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class Language(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    #_user_icon = "//div[@id='fl-overlay-overlay6259']"
    _projectSelect = "//span[contains(text(),'arctest')]"
    _user_icon = "//img[@class='radius']"
    _setting_icon = "//ui-select-options[@class='ui-select--user-menu ng-scope ng-isolate-scope']//li[1]"
    _lang_select = "//ui-select-selected[@class='ng-binding ng-scope']"
    _lang_select_chinese = '''//li[@ng-click="$ctrl.accountSettingsCtrl.setLanguage('zh_cn')"]'''
    _your_profile_chinese = "//h5[contains(text(),'您的个人资料')]"
    _lang_change_english = '''//li[@ng-click="$ctrl.accountSettingsCtrl.setLanguage('en')"]'''

    def selectProject(self):
        self.waitForElement(self._projectSelect, locatorType="xpath")
        self.elementClick(self._projectSelect, locatorType="xpath")

    def clickUserIcon(self):
        self.waitForElement(self._user_icon, locatorType="xpath")
        self.elementClick(self._user_icon, locatorType="xpath")

    def clickSetting(self):
        self.waitForElement(self._setting_icon, locatorType="xpath")
        self.elementClick(self._setting_icon, locatorType="xpath")

    def clickLangDrop(self):
        self.waitForElement(self._lang_select, locatorType="xpath")
        self.elementClick(self._lang_select, locatorType="xpath")

    def selectLangChinese(self):
        self.waitForElement(self._lang_select_chinese, locatorType="xpath")
        self.elementClick(self._lang_select_chinese, locatorType="xpath")

    def verifyLangChange(self):
        result = self.isElementPresent(self._your_profile_chinese, locatorType="xpath")
        return result

    def changeLangToEnglish(self):
        self.clickLangDrop()
        self.waitForElement(self._lang_change_english, locatorType="xpath")
        self.elementClick(self._lang_change_english, locatorType="xpath")

    def SelectLanguage(self):
        self.selectProject()
        time.sleep(4)
        self.clickUserIcon()
        self.clickSetting()
        self.clickLangDrop()
        self.selectLangChinese()









