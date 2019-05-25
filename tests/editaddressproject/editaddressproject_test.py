from pages.editaddressproject.editaddressproject_page import editAddressProject
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class editAddress(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    '''@pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.editap = editAddressProject(self.driver)
        self.ts = TestStatus(self.driver)'''

    @pytest.mark.run(order=1)
    def test_01editAddressProject(self):
        self.editap = editAddressProject(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("Edit the address of project")
        self.log.info("*#" * 20)
        self.editap.Address()
        result = self.editap.verifyAddressChange()
        if result is True:
            self.ts.mark(result, "Address Changes Successfully!!!!!")
        else:
            self.ts.mark(result, "Address Verification Failed!!!!!")




