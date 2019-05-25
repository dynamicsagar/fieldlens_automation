import utilities.custom_logger as cl
from selenium.webdriver.common.action_chains import ActionChains
import logging
from base.basepage import BasePage
import time

class editAddressProject(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators:
    _view_all_project_list = "//a[@class='project view-all ng-binding']"
    _manage_project_button = "//button[@class='generic-button light ng-binding']"
    _hover_map = "//img[@src='https://maps.gstatic.com/mapfiles/api-3/images/google4.png']"
    _map_edit_icon = "//div[@class='columns small-12 manage-project--address manage-project--details-field editable']//i[@class='fa fa-pencil']"
    _address_field = "//input[@placeholder='Address']"
    _unit_field = "//input[@placeholder='Unit']"
    _city_field = "//input[@placeholder='City']"
    _click_green_Check_mark = "//div[@class='manage-projects--save-cancel']//i[@class='fa fa-check']"
    _address_verify = "//span[contains(text(),'162 berlin street')]"


    #Extra:
    _3dot_icon = "//table-row[1]//div[1]//div[2]//div[2]//select-projects-list-overflow-menu[1]//ui-select[1]//div[1]//div[1]//ui-select-selected[1]//img[1]"
    _manage_project = "//ui-select-options[1]//div[1]//div[1]//ul[1]//li[1]"


    def clickAllProject(self):
        self.waitForElement(self._view_all_project_list, locatorType="xpath")
        self.elementClick(self._view_all_project_list, locatorType="xpath")

    #def clickManageProject(self):
        #self.waitForElement(self._manage_project_button, locatorType="xpath")
        #self.elementClick(self._manage_project_button, locatorType="xpath")

    def clickManageProject(self):
        self.waitForElement(self._3dot_icon, locatorType="xpath")
        self.elementClick(self._3dot_icon, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._manage_project, locatorType="xpath")

    def hoverMap(self):
        action = ActionChains(self.driver)
        hover = self.getElement(self._hover_map, locatorType="xpath")
        action.move_to_element(hover).perform()

    def clickMapEditIcon(self):
        self.waitForElement(self._map_edit_icon, locatorType="xpath")
        self.elementClick(self._map_edit_icon, locatorType="xpath")

    def enterAddress(self, address):
        self.waitForElement(self._address_field, locatorType="xpath")
        self.clearField(self._address_field, locatorType="xpath")
        self.sendKeys(address, self._address_field, locatorType="xpath")

    def enterUnit(self, unit):
        self.waitForElement(self._unit_field, locatorType="xpath")
        self.clearField(self._unit_field, locatorType="xpath")
        self.sendKeys(unit, self._unit_field, locatorType="xpath")

    def enterCity(self, city):
        self.waitForElement(self._city_field, locatorType="xpath")
        self.clearField(self._city_field, locatorType="xpath")
        self.sendKeys(city, self._city_field, locatorType="xpath")

    def clickGreenCheckMark(self):
        self.waitForElement(self._click_green_Check_mark, locatorType="xpath")
        self.elementClick(self._click_green_Check_mark, locatorType="xpath")

    def verifyAddressChange(self):
        result = self.isElementPresent(self._address_verify, locatorType="xpath")
        return result

    def Address(self, address="162 berlin street", unit="12345", city="Austin"):
        self.clickAllProject()
        time.sleep(2)
        self.clickManageProject()
        time.sleep(2)
        self.hoverMap()
        time.sleep(0.5)
        self.clickMapEditIcon()
        self.enterAddress(address)
        self.enterUnit(unit)
        self.enterCity(city)
        time.sleep(2)
        self.clickGreenCheckMark()







