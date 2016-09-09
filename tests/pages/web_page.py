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
from selenium.common.exceptions import NoSuchElementException
from tests.pages.base_pages.base_page import BasePage


class WebPage(BasePage):
    """Custom web page representation."""
    NAV_BAR_SELECTOR = 'new UiSelector().textContains("http://www.amazon.com")'
    FOCUSED_WEB_VIEW_SELECTOR = 'new UiSelector().focused(true).descriptionContains("aws")'
    KEYBOARD_ANIMATION_DELAY = 1
    WEBSITE_LOAD_TIME = 7

    def tap_screen_center(self):
        """Taps screen center."""
        window_size = self.driver.get_window_size()
        mid_x = window_size['width'] / 2
        mid_y = window_size['height'] / 2
        self.driver.tap([(mid_x, mid_y)])

    def go_to_url(self, url):
        """Inputs url and presses enter."""
        nav_bar = self.driver.find_element_by_android_uiautomator(self.NAV_BAR_SELECTOR)
        sleep(self.KEYBOARD_ANIMATION_DELAY)  # keyboard will automatically pop up on some devices
        nav_bar.send_keys(url + '\n')
        sleep(self.WEBSITE_LOAD_TIME)

    def web_description_is_loaded(self):
        """Returns visibility of web view with appropriate description.

        Slight work around for consistency: tap the middle of the screen to give the web view focus,
        then check its description.
        """
        self.tap_screen_center()
        try:
            web_view_loaded = self.driver.find_element_by_android_uiautomator(self.FOCUSED_WEB_VIEW_SELECTOR)
            return web_view_loaded.is_displayed()
        except NoSuchElementException:
            return False
