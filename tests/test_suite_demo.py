import unittest
from tests.login.login_test import LoginTests
from tests.newproject.new_project_test import cProject
from tests.downlaodReports.download_report_test import downloadReports
from tests.language.language_test import LanguageChange
from tests.editaddressproject.editaddressproject_test import editAddress
from tests.addpeople.addpeople_test import addPeople
from tests.unreadactivity.global_test import unreadActivityCheck
from tests.post.createeditpost.create_edit_post_test import createUpdatePost
import HtmlTestRunner
import xmlrunner
import os

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(cProject)
tc9 = unittest.TestLoader().loadTestsFromTestCase(cProject)
tc3 = unittest.TestLoader().loadTestsFromTestCase(LanguageChange)
tc4 = unittest.TestLoader().loadTestsFromTestCase(editAddress)
tc5 = unittest.TestLoader().loadTestsFromTestCase(addPeople)
tc6 = unittest.TestLoader().loadTestsFromTestCase(unreadActivityCheck)
tc7 = unittest.TestLoader().loadTestsFromTestCase(createUpdatePost)
tc8 = unittest.TestLoader().loadTestsFromTestCase(downloadReports)



# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8])

dir = os.getcwd()
outfile = open(dir + "SmokeTestReport.html", "w")
#runner = HtmlTestRunner.HTMLTestRunner(output='example_dir')
runner =xmlrunner.XMLTestRunner(output='xml_report_dir')
runner.run(smokeTest)


#unittest.TextTestRunner(verbosity=10).run(smokeTest)
