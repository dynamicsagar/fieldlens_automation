import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class dupPost(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators:
    _projectSelect = "//span[contains(text(),'arctest')]"
    _new_post_button = "//button[@class='generic-button small white create-post-btn ng-binding']"
    _title_field = "//input[@id='ci-title-field']"
    _post_button = "//button[@class='post generic-button blue ng-binding ng-scope']"
    _duplicate_post_checkbox = "//label[@class='fl-checkbox ng-binding']//i"
    _post_duplicate_button = "//button[@class='post generic-button duplicate blue ng-scope ng-isolate-scope']"
    _title_header = "//span[@class='ci-header--title ng-binding']"
    _save_dup_button = "//button[@class='save generic-button duplicate ng-scope ng-isolate-scope']"

    def selectProject(self):
        self.waitForElement(self._projectSelect, locatorType="xpath")
        self.elementClick(self._projectSelect, locatorType="xpath")

    def clickNewPostButton(self):
        self.waitForElement(self._new_post_button, locatorType="xpath")
        self.elementClick(self._new_post_button, locatorType="xpath")

    def enterTitle(self, title):
        self.waitForElement(self._title_field, locatorType="xpath")
        self.sendKeys(title, self._title_field, locatorType="xpath")

    def clickDuplicate(self):
        self.elementClick(self._duplicate_post_checkbox, locatorType="xpath")

    def clickPostDuplicateButton(self):
        self.elementClick(self._post_duplicate_button, locatorType="xpath")

    def duplicatePost(self):
        self.selectProject()
        time.sleep(2)
        self.clickNewPostButton()
        time.sleep(2)
        self.enterTitle("hi")
        time.sleep(2)
        self.clickDuplicate()
        time.sleep(2)
        self.clickPostDuplicateButton()

    def postVerification(self):
        title_text = self.getText(self._title_header,locatorType="xpath")
        #save_dup_button = self.getText(self._post_duplicate_button, locatorType="xpath")
        original_text = 'New post'
        if title_text == original_text:
            return True
        else:
            return False

    #create a draft

    _save_button_ = "//button[@class='save generic-button white ng-binding ng-scope']"
    _close_icon = "//i[@class='fa fa-times']"
    _leave_button_ = "//button[@class='generic-button yellow']"
    _draft_count_ = "//div[@class='fixed-sidebar hide-for-small show-for-medium']//div[@class='ng-scope']//li[1]//span[2]"
    _post_tab_ = "//a[@class='ng-binding active']"

    def clickSaveButton(self):
        self.waitForElement(self._save_button_, locatorType="xpath")
        self.elementClick(self._save_button_,locatorType="xpath")

    def clickTitleCloseIcon(self):
        self.elementClick(self._close_icon, locatorType="xpath")

    def clickLeaveButton(self):
        self.elementClick(self._leave_button_, locatorType="xpath")

    def saveDraft(self):
        time.sleep(5)
        self.clickTitleCloseIcon()
        time.sleep(2)
        self.clickLeaveButton()
        time.sleep(20)
        old_draft = int(self.getText(self._draft_count_, locatorType="xpath"))
        print(old_draft)
        self.clickNewPostButton()
        time.sleep(2)
        self.enterTitle("hi")
        time.sleep(2)
        self.clickSaveButton()
        time.sleep(5)
        self.elementClick(self._post_tab_,locatorType="xpath")
        time.sleep(2)
        new_draft = int(self.getText(self._draft_count_, locatorType="xpath"))
        old_draft = int(old_draft + 1)
        print(old_draft)
        print(new_draft)
        if old_draft == new_draft:
            print("Value matched")
            return True
        else:
            return False



















