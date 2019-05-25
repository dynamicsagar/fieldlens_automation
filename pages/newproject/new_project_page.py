import utilities.custom_logger as cl
from pages.login.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time

class NewProject(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _new_project_button = "//button[@class='generic-button tiny white float-right ng-binding ng-scope']"
    _project_name_field = "//input[@id='project-name']"
    _zipCode_field = "//input[@id='project-postal-code']"
    _create_project_button = "//span[contains(text(),'Create project')]"
    _add_people_field = "//input[@id='add-users-search']"
    _selectPeople = "//span[contains(text(),'sa***@mailinator.com')]"
    _next_button = "//button[@type='button']"
    _gotIt_button = "//button[@class='generic-button ng-binding']"


    def clickNewProjectButton(self):
        self.elementClick(self._new_project_button, locatorType="xpath")

    def enterProjectName(self, text):
        self.sendKeys(text, self._project_name_field,locatorType="xpath")

    def enterZipCode(self, number):
        self.sendKeys(number, self._zipCode_field, locatorType="xpath")

    def clickCreateProjectButton(self):
        self.elementClick(self._create_project_button, locatorType="xpath")

    def enterAddPeople(self, name):
        self.sendKeys(name, self._add_people_field, locatorType="xpath")

    def clickSelectPeople(self):
        self.elementClick(self._selectPeople, locatorType="xpath")

    def clickNextButton(self):
        self.elementClick(self._next_button, locatorType="xpath")

    def clickGotItButton(self):
        self.elementClick(self._gotIt_button, locatorType="xpath")

    def createProject(self, text="", number="", name=""):
        time.sleep(10)
        self.clickNewProjectButton()
        time.sleep(1)
        self.enterProjectName(text)
        time.sleep(0.5)
        self.enterZipCode(number)
        time.sleep(2)
        self.clickCreateProjectButton()
        time.sleep(10)
        self.enterAddPeople(name)
        time.sleep(2)
        self.clickSelectPeople()
        time.sleep(2)
        self.clickNextButton()
        time.sleep(2)
        self.clickNextButton()
        time.sleep(1)
        self.clickGotItButton()

    def verifyProjectCreatedSuccessful(self):
        self.waitForElement("//button[@class='generic-button blue float-right ng-binding']",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//button[@class='generic-button blue float-right ng-binding']",
                                       locatorType="xpath")
        return result

