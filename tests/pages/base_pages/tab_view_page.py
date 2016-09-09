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

from base_page import BasePage


class TabViewPage(BasePage):
    """Base for a tab view page."""
    START_OFFSET = 0.95
    END_OFFSET = 0.05
    SWIPE_DURATION = 1000

    def go_to_next_page(self):
        """Swipes left to go to next page in tab view drawer."""
        size = self.driver.get_window_size()
        start_x = size['width'] * self.START_OFFSET
        end_x = size['width'] * self.END_OFFSET
        mid_y = size['height'] / 2

        self.driver.swipe(start_x, mid_y, end_x, mid_y, self.SWIPE_DURATION)
