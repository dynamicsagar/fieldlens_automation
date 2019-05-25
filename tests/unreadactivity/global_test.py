from pages.unreadactivty.global_page import globalTest
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class unreadActivityCheck(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    '''@pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.activity = globalTest(self.driver)
        self.ts = TestStatus(self.driver)'''

    @pytest.mark.run(order=1)
    def test_01Unread_Activity(self):
        self.activity = globalTest(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("Edit the address of project")
        self.log.info("*#" * 20)
        self.activity.activityUnread()
        result = self.activity.verifyUnreadActivityText()
        if result is True:
            self.ts.mark(result, "Unread Activity Successful")
        else:
            self.ts.mark(result, "Unread Activity Failed")