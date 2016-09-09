# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import unittest
from appium import webdriver
from tests.pages import *


class BaseTest(unittest.TestCase):
    """Basis for all tests."""
    def setUp(self):
        """Sets up desired capabilities and the Appium driver."""
        url = 'http://127.0.0.1:4723/wd/hub'
        desired_caps = {}

        """
        The following desired capabilities must be set when running locally.
        Make sure they are NOT set when uploading to Device Farm.

        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'aPhone'
        """
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'aPhone'
        self.driver = webdriver.Remote(url, desired_caps)
        self.navigation_page = NavigationPage(self.driver)

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()

    def get_name(self):
        raise NotImplementedError

    def navigate_to_page(self):
        """Navigates to desired page."""
        self.navigation_page.go_to_category(self.get_name())
