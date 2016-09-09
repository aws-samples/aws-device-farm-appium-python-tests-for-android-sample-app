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

from tests.pages.base_pages.base_page import BasePage


class AlertsPage(BasePage):
    """Alerts page representation"""
    ALERT_BUTTON_NAME = "ALERT"
    ALERT_MESSAGE_NAME = "This is the alert message"
    OK_BUTTON_NAME = "OK"

    def click_alert_button(self):
        """Taps alert button."""
        alert_button = self.driver.find_element_by_name(self.ALERT_BUTTON_NAME)
        alert_button.click()

    def alert_text_is_displayed(self):
        """Returns visibility of alert's message as a boolean."""
        alert_text = self.driver.find_element_by_name(self.ALERT_MESSAGE_NAME)
        return alert_text.is_displayed()

    def accept_alert_message(self):
        """Taps the OK button to accept the alert."""
        ok_button = self.driver.find_element_by_name(self.OK_BUTTON_NAME)
        ok_button.click()
