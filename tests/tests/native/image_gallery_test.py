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
from tests.pages import ImageGalleryPage


class ImageGalleryTest(NativeTest):
    """Container for all image gallery page tests."""
    PAGE_INDEX = 0

    def setUp(self):
        """Set up Appium connection and navigate to image gallery page."""
        NativeTest.setUp(self)
        NativeTest.navigate_to_page(self)
        self.image_gallery_page = ImageGalleryPage(self.driver)

    def get_page_index(self):
        return PAGE_INDEX

    def test_image_gallery(self):
        """Verifies image gallery is displayed."""
        self.assertTrue(self.image_gallery_page.image_gallery_is_displayed())
