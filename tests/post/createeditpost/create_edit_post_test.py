from pages.post.createeditpost.createeditpost_page import createEditTest
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class createUpdatePost(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    '''@pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.createUpdate = createEditTest(self.driver)
        self.ts = TestStatus(self.driver)'''

    @pytest.mark.run(order=1)
    def test_01title(self):
        self.createUpdate = createEditTest(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("Create and Edit Post")
        self.log.info("*#" * 20)
        self.createUpdate.title()
        result = self.createUpdate.verifyTitlePostString()
        if result is True:
            self.ts.mark(result, "Title Updated Successfully!!!!!")
        else:
            self.ts.mark(result, "Failed to update the Title!!!!!")
            pa
            assert result == False
            #self.assertEqual(act, exp)

    def test_02Watchers(self):
        self.createUpdate = createEditTest(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("Create and Update a post with watchers")
        self.log.info("*#" * 20)
        self.createUpdate.watchers()

    def test_03Description(self):
        self.createUpdate = createEditTest(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("Create and Update a post with description")
        self.log.info("*#" * 20)
        self.createUpdate.description()
        result = self.createUpdate.verifyDescriptionPostString()
        if result is True:
            self.ts.mark(result, "Description Updated Successfully!!!!!")
        else:
            self.ts.mark(result, "Failed to update the description!!!!!")

    def test_04Assignee(self):
        self.createUpdate = createEditTest(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("Create and Update a Assignee")
        self.log.info("*#" * 20)
        self.createUpdate.Assignee()

    def test_05ResourceTracking(self):
        self.createUpdate = createEditTest(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("Create and Update a post with Resource Tracking")
        self.log.info("*#" * 20)
        self.createUpdate.resourceTracking()
        result = self.createUpdate.verifyResourceAdded()
        #assert result == True
        if result is True:
            self.ts.mark(result, "Resource added  Successfully!!!!!")
        else:
            self.ts.mark(result, "Failed to update the Resource tracking!!!!!")

    def test_06Weather(self):
        self.createUpdate = createEditTest(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("Create a POst contains weather")
        self.log.info("*#" * 20)
        self.createUpdate.Weather()
        result = self.createUpdate.verifyWeatherUpdated()
        #assert result == True
        if result is True:
            self.ts.mark(result, "Weather Updated Successfully!!!!!")
        else:
            self.ts.mark(result, "Failed to update the Weather!!!!!")





