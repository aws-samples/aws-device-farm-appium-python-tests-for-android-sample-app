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

from tests.tests.base_tests import NativeTest
from tests.pages import VideoPlayerPage


class VideoPlayerTest(NativeTest):
    """Container for all video player page tests."""
    PAGE_INDEX = 2

    def setUp(self):
        """Set up Appium connection and navigate to video player page."""
        NativeTest.setUp(self)
        NativeTest.navigate_to_page(self)
        self.video_player = VideoPlayerPage(self.driver)

    def get_page_index(self):
        return PAGE_INDEX

    def test_video_player(self):
        """Verifies video is displayed."""
        self.assertTrue(self.video_player.video_is_displayed())
