import utilities.custom_logger as cl
from pages.post.createeditpost.createeditpost_page import createEditTest
from pages.post.DuplicatePost.duplicate_post_page import dupPost
import logging
from base.basepage import BasePage
import time


class CreateRfiSubmittalPost(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ce = createEditTest(self.driver)
        self.dp = dupPost(self.driver)

    #Locators:
    _projectSelect = "//span[contains(text(),'arctest')]"
    _new_post_button = "//button[@class='generic-button small white create-post-btn ng-binding']"
    _title_field = "//input[@id='ci-title-field']"
    _post_button = "//button[@class='post generic-button blue ng-binding ng-scope']"
    _rfi_submittal_text_ = "//div[@class='public-post-message ng-binding ng-scope']"
    _select_rfiFlag = "//li[4]//label[1]"
    _select_submittalFlag = "//li[5]//label[1]"
    _select_dropdown = "//post-flag-single-select[@class='ng-isolate-scope']//div[@class='ui-select--selected ng-scope']"
    _public_icon = "//div[@class='row column collapse post-details--section post-details--current-ccs ng-binding ng-scope']"

    def selectProject(self):
        self.waitForElement(self._projectSelect, locatorType="xpath")
        self.elementClick(self._projectSelect, locatorType="xpath")

    def clickNewPostButton(self):
        self.waitForElement(self._new_post_button, locatorType="xpath")
        self.elementClick(self._new_post_button, locatorType="xpath")

    def enterTitle(self, title):
        self.waitForElement(self._title_field, locatorType="xpath")
        self.sendKeys(title, self._title_field, locatorType="xpath")

    def selectRFIFlag(self):
        self.elementClick(self._select_rfiFlag,locatorType="xpath")

    def selectSubmittal(self):
        self.elementClick(self._select_submittalFlag,locatorType="xpath")

    def clickDropDown(self):
        self.elementClick(self._select_dropdown,locatorType="xpath")


    def testPost(self):
        self.selectProject()
        time.sleep(2)
        self.clickNewPostButton()
        time.sleep(2)
        self.enterTitle("hi")
        time.sleep(2)
        self.clickDropDown()


    def verifyRfiText(self):
        self.testPost()
        time.sleep(2)
        self.selectRFIFlag()
        time.sleep(2)
        rfi_original_text = "RFIs are public, everyone on the project will be able to " \
                            "see them. Once an RFI has been created, " \
                            "it can’t be changed to another post type."
        rfi = self.getText(self._rfi_submittal_text_, locatorType="xpath")
        if rfi == rfi_original_text:
            return True
        else:
            return False

    def verifySubmittalText(self):
        self.clickDropDown()
        time.sleep(2)
        self.selectSubmittal()
        time.sleep(2)
        submittal_original_text = "Submittals are public, everyone on the project will be able to see them. " \
                                  "Once a submittal has been created, it can’t be changed to another post type."
        submittal = self.getText(self._rfi_submittal_text_, locatorType="xpath")
        if submittal_original_text == submittal:
            return True
        else:
            return False

    _add_assign = "//span[@class='ng-binding'][contains(text(),'Assign')]"
    _assignee_select = "//li[2]//div[1]"
    _done_button = "//button[@class='generic-button done ng-binding']"


    def verifyPublicRFiIcon(self):
        self.dp.clickTitleCloseIcon()
        time.sleep(2)
        self.dp.clickLeaveButton()
        time.sleep(2)
        self.ce.clickNewPostButton()
        self.ce.enterTitle('hi')
        time.sleep(5)
        self.elementClick(self._add_assign, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._assignee_select, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._done_button, locatorType="xpath")
        time.sleep(2)
        self.verifyRfiText()
        time.sleep(2)
        self.ce.clickPostButton()
        time.sleep(2)
        self.ce.updateNewToast()
        time.sleep(2)
        self.ce.clickFeedPost()
        icon = self.getText(self._public_icon, locatorType="xpath")
        icon_text = 'Public'
        if icon == icon_text:
            return True
        else:
            return False








