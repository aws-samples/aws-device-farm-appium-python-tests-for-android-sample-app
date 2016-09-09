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
from selenium.common.exceptions import NoSuchElementException


class VideoPlayerPage(BasePage):
    """Video player page representation."""
    VIDEO_VIEW_CLASS = 'android.widget.VideoView'
    BAD_VIDEO_ALERT_NAME = "Can't play this video."

    def video_is_displayed(self):
        """Returns visibility of video as boolean.

        Media player is incompatible with a small number of devices,
        checks for "Can't play this video" alert in this case.
        """
        try:
            video_element = self.driver.find_element_by_class_name(self.VIDEO_VIEW_CLASS)
        except NoSuchElementException:
            video_element = self.driver.find_element_by_name(self.BAD_VIDEO_ALERT_NAME)

        return video_element.is_displayed()
