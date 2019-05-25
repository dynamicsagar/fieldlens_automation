import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class createEditTest(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators:
    _projectSelect = "//span[contains(text(),'arctest')]"
    _new_post_button = "//button[@class='generic-button small white create-post-btn ng-binding']"
    _title_field = "//input[@id='ci-title-field']"
    _post_button = "//button[@class='post generic-button blue ng-binding ng-scope']"
    _click_post = "//table-row[1]//div[1]//div[3]"
    _edit_icon = "//*[@class='fl-action-icon edit']"
    _edit_title = "//ui-select-options[@class='post-overflow-edit-options ng-scope ng-isolate-scope']//li[2]"
    _update_title = "//input[@placeholder='Enter a title (required)']"
    _update_button = "//span[@class='ng-binding'][contains(text(),'Update')]"
    _close_icon = "//i[@class='fa fa-times']"
    _title_post_string = '''//span[contains(text(),'Renamed title from "hi" to "hi with title update"')]'''

    def selectProject(self):
        self.waitForElement(self._projectSelect, locatorType="xpath")
        self.elementClick(self._projectSelect, locatorType="xpath")

    def clickNewPostButton(self):
        self.waitForElement(self._new_post_button, locatorType="xpath")
        self.elementClick(self._new_post_button, locatorType="xpath")

    def enterTitle(self, title):
        self.waitForElement(self._title_field, locatorType="xpath")
        self.sendKeys(title, self._title_field, locatorType="xpath")

    def clickPostButton(self):
        self.waitForElement(self._post_button, locatorType="xpath")
        self.elementClick(self._post_button, locatorType="xpath")

    def updateNewToast(self):
        self.waitForElement(self._new_update_button, locatorType="xpath")
        self.elementClick(self._new_update_button, locatorType="xpath")

    def clickFeedPost(self):
        self.waitForElement(self._click_post, locatorType="xpath")
        self.elementClick(self._click_post, locatorType="xpath")

    def clickEditIcon(self):
        self.waitForElement(self._edit_icon, locatorType="xpath")
        self.elementClick(self._edit_icon, locatorType="xpath")

    def clickEditTitle(self):
        self.waitForElement(self._edit_title, locatorType="xpath")
        self.elementClick(self._edit_title, locatorType="xpath")

    def updateTitle(self, updateTitle):
        self.clearField(self._update_title, locatorType="xpath")
        self.sendKeys(updateTitle, self._update_title, locatorType="xpath")

    def clickUpdateTitleButton(self):
        self.elementClick(self._update_button, locatorType="xpath")

    def clickTitleCloseIcon(self):
        self.elementClick(self._close_icon, locatorType="xpath")

    def gUseForall(self):
        self.clickPostButton()
        time.sleep(2)
        self.updateNewToast()
        time.sleep(5)
        self.clickFeedPost()
        self.clickEditIcon()

    def title(self, title="hi", updatedTitle="hi with title update"):
        self.selectProject()
        self.clickNewPostButton()
        self.enterTitle(title)
        time.sleep(2)
        self.gUseForall()
        self.clickEditTitle()
        self.updateTitle(updatedTitle)
        self.clickUpdateTitleButton()


    def verifyTitlePostString(self):
        updated_title = 'Renamed title from "hi" to "hiwith title update"'
        post_string = self.getText(self._title_post_string, locatorType="xpath")
        if updated_title == post_string:
            print(post_string)
            return True
        #result = self.isElementPresent(self._title_post_string, locatorType="xpath")
        #self.clickTitleCloseIcon()
        #return result

    #######################################################################################################
    # watchers
    _to_field = "//input[@id='ci-watchers-field']"
    _browser_button = "//div[@id='ci-watchers']//a[@class='browse-pill ng-binding'][contains(text(),'Browse')]"
    _email_field = "//span[contains(text(),'Enter a name, email, or company')]"
    _select_email_result = "//div[@class='row column body']//li[1]"
    _done_button = "//button[@class='generic-button done ng-binding']"
    _new_update_button = "//div[@class='post-feed--updates-available ng-binding post-feed--updates-available-visible']"
    _edit_sent_to = "//ui-select-options[@class='post-overflow-edit-options ng-scope ng-isolate-scope']//li[1]"
    _browse_edit_button = "//span[@class='splink browse ng-binding']"
    _select_people_list = "//recipients-user-row[2]//label[1]//div[2]"
    _submit_button = "//button[@class='generic-button blue ng-binding']"
    _watchers_update_button = "//button[@class='generic-button blue']"
    _post_reaction_string = "//span[contains(text(),'Added !!Amit !!Amit')]"

    def clickBrowser(self):
        self.waitForElement(self._browser_button, locatorType="xpath")
        self.elementClick(self._browser_button, locatorType="xpath")

    def clickEmailWatcher(self):
        self.elementClick(self._select_email_result, locatorType="xpath")

    def clickDoneButton(self):
        self.elementClick(self._done_button, locatorType="xpath")

    def clickEditSentTo(self):
        self.waitForElement(self._edit_sent_to, locatorType="xpath")
        self.elementClick(self._edit_sent_to, locatorType="xpath")

    def clickBrowseButton(self):
        self.elementClick(self._browse_edit_button, locatorType="xpath")

    def selectPeople(self):
        self.elementClick(self._select_people_list, locatorType="xpath")

    def clickSubmitButton(self):
        self.elementClick(self._submit_button, locatorType="xpath")

    def clickUpdateWatcherButton(self):
        self.elementClick(self._watchers_update_button, locatorType="xpath")

    #Create and Update a post with watchers
    def watchers(self, title="Watchers with send to"):
        time.sleep(2)
        self.clickNewPostButton()
        self.enterTitle(title)
        self.clickBrowser()
        self.clickEmailWatcher()
        self.clickDoneButton()
        time.sleep(2)
        self.gUseForall()
        self.clickEditSentTo()
        time.sleep(2)
        self.clickBrowseButton()
        self.selectPeople()
        self.clickSubmitButton()
        time.sleep(2)
        self.clickUpdateWatcherButton()
        time.sleep(5)
        self.clickTitleCloseIcon()


    #description
    _description_field = "//textarea[@placeholder='Add more details here…']"
    _edit_description = "//ui-select-options[@class='post-overflow-edit-options ng-scope ng-isolate-scope']//li[3]"
    _add_location = "//ui-select-options[@class='post-overflow-edit-options ng-scope ng-isolate-scope']//li[4]"
    _add_post_flag = "//ui-select-options[@class='post-overflow-edit-options ng-scope ng-isolate-scope']//li[5]"
    _add_drawing = "//ui-select-options[@class='post-overflow-edit-options ng-scope ng-isolate-scope']//li[6]"
    _add_categories = "//ui-select-options[@class='post-overflow-edit-options ng-scope ng-isolate-scope']//li[7]"
    _description_update_button = "//span[@class='ng-binding'][contains(text(),'Update')]"
    # addEditDescription:
    _update_description = "//textarea[@placeholder='Add a description (optional)']"
    _update_description_string = "//span[@class='splink ng-binding']"

    def enterDescription(self, desc):
        self.waitForElement(self._description_field, locatorType="xpath")
        self.sendKeys(desc, self._description_field, locatorType="xpath")

    def clickEditDescription(self):
        self.elementClick(self._edit_description, locatorType="xpath")

    def enterUpdatedDescription(self, updatedDescription):
        self.waitForElement(self._update_description, locatorType="xpath")
        self.sendKeys(updatedDescription, self._update_description, locatorType="xpath")

    def clickDescriptionUpdateButton(self):
        self.elementClick(self._description_update_button, locatorType="xpath")


    def description(self, title = "We are automating description", descr = "description text", updatedes="description text has been updated"):
        time.sleep(2)
        self.clickNewPostButton()
        self.enterTitle(title)
        self.enterDescription(descr)
        time.sleep(2)
        self.gUseForall()
        time.sleep(2)
        self.clickEditDescription()
        self.enterUpdatedDescription(updatedes)
        time.sleep(2)
        self.clickDescriptionUpdateButton()


    def verifyDescriptionPostString(self):
        result = self.isElementPresent(self._update_description_string, locatorType="xpath")
        time.sleep(2)
        self.clickTitleCloseIcon()
        return result


    #updateAssignee
    _update_assignee_button = "//span[@class='content-pill pill--assign ng-binding pill--transparent']"
    _update_assignee_textfield = "//span[@class='helper-text browse ng-binding ng-scope']"
    _select_assignee = "//select-assignable-user-row[1]//label[1]//div[1]//span[1]//i[1]"
    _assignee_done_button = "//button[contains(text(),'Done')]"
    _assignee_update_button = "//button[@type='button']"
    _updated_Assignee_string = "//span[contains(text(),'Added 0412 Fieldlens as an assignee')]"

    def clickUpdateAssigneeButton(self):
        self.elementClick(self._update_assignee_button, locatorType="xpath")

    def clickAssigneeBrowse(self):
        self.elementClick(self._update_assignee_textfield, locatorType="xpath")

    def clickAssigneeFromList(self):
        self.elementClick(self._select_assignee, locatorType="xpath")

    def clickAssigneeDoneButton(self):
        self.elementClick(self._assignee_done_button, locatorType="xpath")

    def clickAssigneeUpdateButton(self):
        self.elementClick(self._assignee_update_button, locatorType="xpath")

    def Assignee(self, title="updateAssignee"):
        time.sleep(2)
        self.clickNewPostButton()
        self.enterTitle(title)
        self.clickBrowser()
        self.clickEmailWatcher()
        self.clickDoneButton()
        time.sleep(2)
        self.clickPostButton()
        time.sleep(2)
        self.updateNewToast()
        time.sleep(5)
        self.clickFeedPost()
        time.sleep(1)
        self.clickUpdateAssigneeButton()
        time.sleep(0.5)
        self.clickAssigneeBrowse()
        self.clickAssigneeFromList()
        self.clickAssigneeDoneButton()
        time.sleep(1)
        self.clickAssigneeUpdateButton()
        time.sleep(2)
        self.clickTitleCloseIcon()


    #pin to drawing
    pin_drawing_icon = "//*[@class='fl-action-icon pin-to-drawing']"


    #add location
    _location_icon = "//li[@class='action-type hint hint--top hint--rounded']//*[@class='fl-action-icon location']"
    _location_add = "//input[@id='add-level-0']"
    _green_Check = "//i[@class='fa fa-check']"


    #add resource tracking
    _resource_tracking = "//li[@class='action-type hint hint--top hint--rounded']//*[@class='fl-action-icon manpower']"
    _select_resource_button = "//button[@class='select-button ng-binding']"
    _ad_resource = "//li[1]//div[1]"
    _ad_res_firstname = "//input[@placeholder='*First Name']"
    _ad_res_lastname = "//input[@placeholder='*Last Name']"
    _ad_res_submit_button = "//button[@type='submit']"
    _ad_res_companies = "//li[@class='ng-binding ng-scope selected']"
    ad_res_select_company = "//div[@class='columns large-7']//li[1]//div[1]"
    _ad_res_discipline = "//li[contains(text(),'Disciplines')]"
    ad_res_dis_select = "//div[contains(text(),'Designer / Consultant')]"
    ad_res_click_disp = "//div[@class='columns large-7']//li[1]//div[1]"
    resource_submit_button = "//button[@class='generic-button done ng-binding']"
    _resource_verification = "//div[@class='columns small-3 ng-binding']"


    def clickResourceTrackingIcon(self):
        self.elementClick(self._resource_tracking, locatorType="xpath")

    def clickResourceButton(self):
        self.elementClick(self._select_resource_button, locatorType="xpath")

    def clickAddResource(self):
        self.elementClick(self._ad_resource, locatorType="xpath")

    def clickResourceDoneButton(self):
        self.elementClick(self.resource_submit_button, locatorType="xpath")


    def resourceTracking(self, title="Resource Tracking"):
        time.sleep(3)
        self.clickNewPostButton()
        self.enterTitle(title)
        self.clickResourceTrackingIcon()
        self.clickResourceButton()
        self.clickAddResource()
        self.clickResourceDoneButton()
        time.sleep(2)
        self.clickPostButton()
        time.sleep(2)
        self.updateNewToast()
        time.sleep(5)
        self.clickFeedPost()

    def verifyResourceAdded(self):
        result = self.isElementPresent(self._resource_verification, locatorType="xpath")
        self.clickTitleCloseIcon()
        return result

    #Weather
    _add_weather_icon = "//*[@class='fl-action-icon weather']"
    _add_weather_repost = "//span[@class='content-pill pill--weather ng-binding pill--transparent']"
    _update_weather_button = "//button[@class='generic-button blue ng-binding']"
    _verify_weather_updated = "//span[@class='action-description text-left ng-binding ng-scope']"


    def clickWeatherIcon(self):
        self.elementClick(self._add_weather_icon, locatorType="xpath")

    def clickWeatherRepost(self):
        self.elementClick(self._add_weather_repost, locatorType="xpath")

    def clickUpdateWeatherButton(self):
        self.elementClick(self._update_weather_button, locatorType="xpath")


    def Weather(self, title ="Weather"):
        time.sleep(2)
        self.clickNewPostButton()
        self.enterTitle(title)
        self.clickWeatherIcon()
        time.sleep(2)
        self.clickDoneButton()
        self.clickPostButton()
        time.sleep(2)
        self.updateNewToast()
        time.sleep(5)
        self.clickFeedPost()
        time.sleep(1)
        self.clickWeatherRepost()
        time.sleep(0.5)
        self.clickUpdateWeatherButton()

    def verifyWeatherUpdated(self):
        result = self.isElementPresent(self._verify_weather_updated, locatorType="xpath")
        self.clickTitleCloseIcon()
        return result



























