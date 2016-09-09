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

from time import sleep
from tests.pages.base_pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page representation."""
    USERNAME_FIELD_ID = 'Username Input Field'
    PASSWORD_FIELD_ID = 'Password Input Field'
    ALT_MESSAGE_ID = 'Alt Message'
    ALT_BUTTON_ID = 'Alt Button'
    LOG_IN_BUTTON_ID = 'Login Button'
    KEYBOARD_ANIMATION_DELAY = 1

    def log_in(self, username, password):
        """Types in inputted username and password and presses log in button."""
        username_field = self.driver.find_element_by_id(self.USERNAME_FIELD_ID)
        password_field = self.driver.find_element_by_id(self.PASSWORD_FIELD_ID)
        log_in_button = self.driver.find_element_by_id(self.LOG_IN_BUTTON_ID)

        username_field.click()
        sleep(self.KEYBOARD_ANIMATION_DELAY)
        username_field.send_keys(username)

        password_field.click()
        sleep(self.KEYBOARD_ANIMATION_DELAY)
        password_field.send_keys(password)

        log_in_button.click()

    def get_message(self):
        """Returns the post-login page message."""
        message = self.driver.find_element_by_id(self.ALT_MESSAGE_ID)
        return message.text

    def click_alt_button(self):
        """Tap try again or log in button."""
        alt_button = self.driver.find_element_by_id(self.ALT_BUTTON_ID)
        alt_button.click()

    def is_at_login(self):
        """Returns whether or not we are back at the original login view as a boolean.

        Simply checks for the visibility of the login button.
        """
        log_in_button = self.driver.find_element_by_id(self.LOG_IN_BUTTON_ID)
        return log_in_button.is_displayed()
