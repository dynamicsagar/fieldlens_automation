import utilities.custom_logger as cl
from pages.login.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time

class Reports(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _projectSelect = "//span[contains(text(),'arctest')]"
    _searchProject = "//input[@placeholder='Search All Projects']"
    _selectProject = "//span[@class='project-name-placeholder']"
   # _exportReport_button = "//button[@class='create-report generic-button small blue float-right ng-binding ng-scope']"
    _reportClick = ""
    _dotIcon = "//table-row[1]//div[1]//div[2]//div[4]//reports-management-overflow-menu[1]//ui-select[1]//div[1]//div[1]//ui-select-selected[1]//img[1]"
    _downloadReport = "//a[@title='Download Report']"
    _rerunReport = "//i[@class='fa fa-refresh']"
    _goiIt_button = "//button[contains(.,'Got it')]"

    def selectProject(self):
        self.waitForElement(self._projectSelect, locatorType="xpath")
        self.elementClick(self._projectSelect, locatorType="xpath")

    def clickReportExportButton(self):
        self.waitForElement("", locatorType="xpath")
        self.elementClick(self._exportReport_button,locatorType="xpath")

    def clickReport(self):
        self.elementClick(self._reportClick, locatorType="xpath")

    def clickDotIcon(self):
        self.waitForElement(self._dotIcon, locatorType="xpath")
        self.elementClick(self._dotIcon, locatorType="xpath")

    def clickDownloadReport(self):
        self.waitForElement(self._downloadReport, locatorType="xpath")
        self.elementClick(self._downloadReport, locatorType="xpath")

    def clickRerunReport(self):
        self.waitForElement(self._rerunReport, locatorType="xpath")
        self.elementClick(self._rerunReport, locatorType="xpath")

    def clickGotItButton(self):
        self.waitForElement(self._goiIt_button, locatorType="xpath")
        self.elementClick(self._goiIt_button, locatorType="xpath")

    def report(self):
        self.selectProject()
        self.nav.navigateToReports()
        time.sleep(5)
        self.clickDotIcon()

    def downloadReport(self):
        self.report()
        time.sleep(1)
        self.clickDownloadReport()

    def downloadRerunReport(self):
        self.report()
        self.clickRerunReport()
        self.clickGotItButton()

    def verifyRerunFunctionality(self):
        self.waitForElement("//div[@class='columns small-12 text-center ng-binding']",
                            locatorType="xpath")
        results = self.isElementPresent(locator="//div[@class='columns small-12 text-center ng-binding']",
                                        locatorType="xpath")
        return results

