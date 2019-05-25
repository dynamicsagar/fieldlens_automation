from pages.language.language_page import Language
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LanguageChange(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    '''@pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)'''

    @pytest.mark.run(order=1)
    def test_t1LanguageVerification(self):
        self.lang.SelectLanguage()
        result = self.lang.verifyLangChange()
        if result is True:
            self.lang.changeLangToEnglish()
            time.sleep(15)
            self.ts.mark(result, "Language change Verification successfully !!!!")
        else:
            self.ts.mark(result, "Unable to change the language")


