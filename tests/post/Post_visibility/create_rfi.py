from pages.post.post_visibility.create_rfi import CreateRfiSubmittalPost
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class rfiSubmittal(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def test_01RFI(self):
        self.post = CreateRfiSubmittalPost(self.driver)
        result = self.post.verifyRfiText()
        assert result == True

    def test_02Submittal(self):
        self.post = CreateRfiSubmittalPost(self.driver)
        result = self.post.verifySubmittalText()
        assert result == True

    def test_03CreateRfiPost(self):
        self.post = CreateRfiSubmittalPost(self.driver)
        result = self.post.verifyPublicRFiIcon()
        assert result == True




