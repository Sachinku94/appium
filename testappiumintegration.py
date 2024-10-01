# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
# from utilities.base_class import BaseClass

# import pytest
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
# import time


# class Testone(BaseClass):

#   def test_demo1(self):

#     time.sleep(20)

#     self.driver.find_element(AppiumBy.ID, "com.android.chrome:id/signin_fre_dismiss_button").click()

#     time.sleep(20)  # Wait for the input field to become active

#     self.driver.find_element(AppiumBy.ID,"com.android.chrome:id/negative_button").click()
#     time.sleep(20)


#     self.driver.find_element(AppiumBy.ID,"com.android.chrome:id/search_box_text").send_keys("sachin")
#     # Press the Enter key
#     self.driver.press_keycode(66)

#     time.sleep(40)
from appium.webdriver.common.appiumby import AppiumBy
from utilities.base_class import BaseClass
import pytest
import time


@pytest.mark.usefixtures("setup")  # Apply the setup fixture to this test class
class Testone(BaseClass):

    def test_demo1(self):
        time.sleep(20)

        # Dismiss the sign-in prompt
        self.driver.find_element(
            AppiumBy.ID, "com.android.chrome:id/signin_fre_dismiss_button"
        ).click()

        time.sleep(40)  # Wait for the input field to become active

        # Dismiss the negative button
        self.driver.find_element(
            AppiumBy.ID, "com.android.chrome:id/ack_button"
        ).click()
        time.sleep(20)

        # Enter text in the search box
        self.driver.find_element(
            AppiumBy.ID, "com.android.chrome:id/search_box_text"
        ).send_keys("sachin")

        # Press the Enter key
        self.driver.press_keycode(66)

        time.sleep(40)
