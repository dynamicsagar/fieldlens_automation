from pages.post.DuplicatePost.duplicate_post_page import dupPost
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class dupliPost(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def test_01duplicate(self):
        self.dp = dupPost(self.driver)
        self.dp.duplicatePost()
        time.sleep(2)
        result = self.dp.postVerification()
        assert result == True
        #self.ts.markFinal("test_project", result, "Project created successfully.")


    def test_02save(self):
        self.dp = dupPost(self.driver)
        result = self.dp.saveDraft()
        assert result == True
        print("pass")





