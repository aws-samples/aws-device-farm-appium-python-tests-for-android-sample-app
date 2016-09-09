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


class ImageGalleryPage(BasePage):
    """Image gallery page representation."""
    GRID_VIEW_CLASS = 'android.widget.GridView'

    def image_gallery_is_displayed(self):
        """Returns visibility of image gallery as a boolean."""
        image_gallery = self.driver.find_element_by_class_name(self.GRID_VIEW_CLASS)
        return image_gallery.is_displayed()
