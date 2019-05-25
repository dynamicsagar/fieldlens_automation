from pages.login.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    '''@pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)'''

    @pytest.mark.run(order=1)
    def test_t1invalidLogin(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.login("sagar01+fieldlens@mailinator.com", "43434")
        time.sleep(2)
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_t2validLogin(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.login("sagar01+fieldlens@mailinator.com", "12345678")
        time.sleep(2)
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.markFinal("test_t2validLogin", result2, "Login Verification")