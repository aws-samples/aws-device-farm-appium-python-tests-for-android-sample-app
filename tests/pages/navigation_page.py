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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions


class NavigationPage(BasePage):
    """Class that handles navigation to different pages within the application."""
    NAV_DRAWER_TOGGLE_ID = 'ReferenceApp'
    RECYCLER_VIEW_ID = 'drawerList'
    NAV_DRAWER_ANIMATION_DELAY = 2
    MAX_ATTEMPTS = 5

    def scroll_nav_drawer_down(self):
        """Scroll the navigation drawer down."""
        recycler_view = self.driver.find_element_by_id(self.RECYCLER_VIEW_ID)

        recycler_location_x = recycler_view.location['x']
        recycler_location_y = recycler_view.location['y']

        recycler_x_offset = recycler_view.size['width'] / 2
        recycler_height = recycler_view.size['height']
        recycler_y_start_offset = recycler_height * .95
        recycler_y_end_offset = recycler_height * .05

        mid_x = recycler_location_x + recycler_x_offset
        start_y = recycler_location_y + recycler_y_start_offset
        end_y = recycler_location_y + recycler_y_end_offset

        action = TouchActions(self.driver)
        action.tap_and_hold(mid_x, start_y).move(mid_x, end_y).release(mid_x, end_y).perform()

    def go_to_category(self, category_name):
        """Clicks appropriate button in the navigation drawer."""
        self.driver.find_element_by_accessibility_id(self.NAV_DRAWER_TOGGLE_ID).click()
        sleep(self.NAV_DRAWER_ANIMATION_DELAY)

        category_element = None
        num_attempts = 0

        while category_element is None and num_attempts < self.MAX_ATTEMPTS:
            try:
                category_element = self.driver.find_element_by_name(category_name)
                num_attempts += 1
            except NoSuchElementException:
                self.scroll_nav_drawer_down()

        category_element.click()
