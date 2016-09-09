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

from base_tests.base_test import BaseTest
from tests.pages import AlertsPage


class AlertsTest(BaseTest):
    """Container for all alerts page tests."""
    PAGE_NAME = 'Alerts'

    def setUp(self):
        """Set up Appium connection and navigate to image gallery page."""
        BaseTest.setUp(self)
        BaseTest.navigate_to_page(self)
        self.alerts = AlertsPage(self.driver)

    def get_name(self):
        return PAGE_NAME

    def test_alert(self):
        """Clicks alert button, verifies alert text, accepts the alert message."""
        self.alerts.click_alert_button()
        self.assertTrue(self.alerts.alert_text_is_displayed())
        self.alerts.accept_alert_message()
