from pages.addpeople.add_people_page import AddPeople
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class addPeople(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ap = AddPeople(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_01addNewPeople(self):
        self.log.info("*#" * 20)
        self.log.info("People adding started")
        self.log.info("*#" * 20)
        email = self.ap.util.getUniqueName()
        result = self.ap.verifyNewPeopleAdded(email + "@gmail.com")
        print("Result1: " + str(result))
        #assert result == True
        #self.ts.markFinal("test_addNewPeople", result, "People added successfully")

    #@pytest.mark.run(order=2)
    #def test_verifyPeopleAdded(self):
        #self.log.info("*#" * 20)
        #self.log.info("People added text verification started")
        #self.log.info("*#" * 20)
        #email = self.ap.util.getUniqueName()
        #result = self.ap.verifyNewPeopleAddedText(email + "@gmail.com")


    @pytest.mark.run(order=2)
    def test_02addAlreadyAddedPeople(self):
        self.log.info("*#" * 20)
        self.log.info("Select already added people started")
        self.log.info("*#" * 20)
        self.ap.addAlreadyAddedPeople()

    #@pytest.mark.run(order=4)
    #def test_verifyAlreadyAddedPeople(self):
        #self.log.info("*#" * 20)
        #self.log.info("Verify already added People text")
        #self.log.info("*#" * 20)
        #result = self.ap.verifyAddedPeopleText()
        #assert result == True
        #self.ts.markFinal("test_verifyAlreadyAddedPeople", result, "Already added people text verified")

    def test_03SelectFilterFromDropdown(self):
        self.ap.filterFunctionality()












