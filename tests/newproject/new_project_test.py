from pages.newproject.new_project_page import NewProject
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class cProject(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)

    def test_project(self):
        self.pr = NewProject(self.driver)
        self.log.info("*#" * 20)
        self.log.info("verify project created successfully")
        self.log.info("*#" * 20)
        self.pr.createProject("firstAuto", "99501", "sagar")
        result = self.pr.verifyProjectCreatedSuccessful()
        assert result == True
        self.ts.markFinal("test_project", result, "Project created successfully.")
