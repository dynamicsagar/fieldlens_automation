import utilities.custom_logger as cl
from pages.login.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time


class AddPeople(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    ##########################################################################
    # Select filter Locator 2
    #_click_filter_dropdown = "//ui-select-selected[@class='ng-scope']//div[@class='ng-scope']"
    _click_filter_dropdown = "//ui-select[@class='directory-filter--directory-filter-select ng-isolate-scope ui-select--menu ui-select--close-on-click show-notification']//div[@class='ui-select--selected ng-scope']"
    _click_my_company_dropdown = "//li[2]//div[1]"
    _click_clearFilter_button = "//span[contains(text(),'Clear')]"

    # Filters functionality
    def clickFilter(self):
        self.waitForElement(self._click_filter_dropdown, locatorType="xpath")
        self.elementClick(self._click_filter_dropdown, locatorType="xpath")

    def selectMyCompany(self):
        self.waitForElement(self._click_my_company_dropdown, locatorType="xpath")
        self.elementClick(self._click_my_company_dropdown, locatorType="xpath")

    def clickClearButton(self):
        self.isElementDisplayed(self._click_clearFilter_button, locatorType="xpath")
        self.elementClick(self._click_clearFilter_button, locatorType="xpath")
        sa = self.getElement(self._click_clearFilter_button, locatorType="xpath")
        if sa.is_enabled():
            print("button find")
            self.log.info("button active")
        else:
            print("fail")

    def filterFunctionality(self):
        time.sleep(5)
        self.clickFilter()
        time.sleep(1)
        self.selectMyCompany()
        time.sleep(2)
        self.clickClearButton()

    ########################################################################################

    # Locators
    _projectSelect = "//span[contains(text(),'arctest')]"
    _add_peopletoproject_button = "//button[@class='generic-button blue float-right ng-binding']"
    _enter_email_field = "//input[@placeholder='Search Fieldlens or add a new email']"
    _click_email_field = "//span[@class='content-pill pill--email ng-binding']"
    _select_people = "//div[@class='fl-condensed-list']//div[1]//div[1]//div[1]"
    _next_button = "//button[@type='button']"
    _not_now_button = "//button[contains(text(),'Not now')]"
    _add_profile_info_button = "//button[contains(text(),'Add profile info')]"
    _new_person_added_text = "//div[@class='message-view-editable'][contains(text(),'Next: Add missing profile info for  1  person .' )]"
    _gotit_button = "//button[@class='generic-button ng-binding']"
    _user_already_added = "//div[@class='message-success']"


    def selectProject(self):
        self.waitForElement(self._projectSelect, locatorType="xpath")
        self.elementClick(self._projectSelect, locatorType="xpath")

    def addPeopleToProject(self):
        self.waitForElement(self._add_peopletoproject_button, locatorType="xpath")
        self.elementClick(self._add_peopletoproject_button, locatorType="xpath")

    def enterEmail(self, email):
        self.waitForElement(self._enter_email_field, locatorType="xpath")
        self.sendKeys(email, self._enter_email_field, locatorType="xpath")

    def clickEmail(self):
        self.elementClick(self._click_email_field, locatorType="xpath")

    def selectPeople(self):
        #self.sendKeys(email, self._enter_email_field, locatorType="xpath")
        time.sleep(0.5)
        self.elementClick(self._select_people, locatorType="xpath")

    def clickNextButton(self):
        self.waitForElement(self._next_button, locatorType="xpath")
        self.elementClick(self._next_button, locatorType="xpath")

    def clickNotNowButton(self):
        self.waitForElement(self._not_now_button, locatorType="xpath")
        self.elementClick(self._not_now_button, locatorType="xpath")

    def clickGotItButton(self):
        self.waitForElement(self._gotit_button, locatorType="xpath")
        self.elementClick(self._gotit_button, locatorType="xpath")


    def add_People_To_Project(self, email):
        self.selectProject()
        self.nav.navigateToPeople()
        self.addPeopleToProject()
        self.enterEmail(email)
        self.clickEmail()
        self.clickNextButton()
        self.clickNextButton()

    def add_alreadyAddedPeopleToProject(self):
        #self.selectProject()
        #self.nav.navigateToPeople()
        time.sleep(2)
        self.addPeopleToProject()
        time.sleep(2)
        self.selectPeople()
        self.clickNextButton()
        time.sleep(2)
        self.clickNextButton()


    def verifyNewPeopleAddedText(self, email):
        self.add_People_To_Project(email)
        result = self.isElementPresent(self._new_person_added_text, locatorType="xpath")
        result_1 = self.isElementPresent(self._add_profile_info_button, locatorType="xpath")
        return result, result_1
        #if result == True:
        #    print("PEOPLE ADDED TO PROJECT SUCCESSFULLY!!!!!")
        #    return result
        #else:
        #    print("Verification failed!!!!")

    def verifyNewPeopleAdded(self, email):
        self.add_People_To_Project(email)
        time.sleep(2)
        self.clickNotNowButton()


    def verifyAddedPeopleText(self):
        self.add_alreadyAddedPeopleToProject()
        result = self.isElementPresent(self._user_already_added, locatorType="xpath")
        return result

    def addAlreadyAddedPeople(self):
        self.add_alreadyAddedPeopleToProject()
        time.sleep(2)
        self.clickGotItButton()

    def logout(self):
        logoutLinkElement = self.waitForElement(locator="//img[@class='radius']",
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
        time.sleep(2)
        self.elementClick(locator="//ui-select-options[@class='ui-select--user-menu ng-scope ng-isolate-scope']//li[5]",
                          locatorType="xpath")

















