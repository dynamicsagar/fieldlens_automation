from pages.downloadReports.download_report_page import Reports
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class downloadReports(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.re = Reports(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_DownloadReports(self):
        self.re.downloadReport()


    @pytest.mark.run(order=2)
    def test_RerunReports(self):
        self.re.downloadRerunReport()
        result1 = self.re.verifyRerunFunctionality()
        assert result1 == True
        print("Result1: " + str(result1))
        self.ts.markFinal("test_RerunReports", result1, "Report Downloaded Successfully")















