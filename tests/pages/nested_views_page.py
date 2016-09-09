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


class NestedViewsPage(BasePage):
    """Nested views page representation."""
    UP_NAVIGATION_NAME = 'UP NAVIGATION'
    BACK_NAVIGATION_NAME = 'BACK NAVIGATION'
    FIRST_LEVEL_TEXT_NAME = 'Press to go to the next level'
    FINAL_LEVEL_TEXT_NAME = 'Final Level'
    NEXT_LEVEL_BUTTON_NAME = 'NEXT LEVEL'
    COUNTER_NAME = 'Level Display'
    UP_NAVIGATION_BACK_BUTTON_NAME = 'Navigate up'

    def press_up_navigation(self):
        """Press up navigation button."""
        up_navigation = self.driver.find_element_by_name(self.UP_NAVIGATION_NAME)
        up_navigation.click()

    def press_back_navigation(self):
        """Press back navigation button."""
        back_navigation = self.driver.find_element_by_name(self.BACK_NAVIGATION_NAME)
        back_navigation.click()

    def first_level_text_is_displayed(self):
        """Returns visibility of first level text as a boolean."""
        first_level_text = self.driver.find_element_by_name(self.FIRST_LEVEL_TEXT_NAME)
        return first_level_text.is_displayed()

    def final_level_text_is_displayed(self):
        """Returns visibility of final level text as a boolean."""
        final_level_text = self.driver.find_element_by_name(self.FINAL_LEVEL_TEXT_NAME)
        return final_level_text.is_displayed()

    def press_up_navigation_back_button(self):
        """Press up navigation back button."""
        back_button = self.driver.find_element_by_id(self.UP_NAVIGATION_BACK_BUTTON_NAME)
        back_button.click()

    def press_next_level(self):
        """Press next level button."""
        next_level_button = self.driver.find_element_by_name(self.NEXT_LEVEL_BUTTON_NAME)
        next_level_button.click()

    def get_counter(self):
        """Returns the current page counter as an int."""
        counter = self.driver.find_element_by_name(self.COUNTER_NAME)
        return int(counter.text)

    def press_back_button(self):
        """Press phone's back button."""
        self.driver.back()
