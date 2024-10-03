from appium.webdriver.common.appiumby import AppiumBy
from utilities.base_class import BaseClass
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")  # Apply the setup fixture to this test class
class Testone(BaseClass):

    def test_demoappsignup(self):

        time.sleep(20)
        wait = WebDriverWait(
            self.driver, 30, poll_frequency=5, ignored_exceptions=[TimeoutException]
        )
        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer"
        ).click()

        My_account = self.driver.find_element(
            AppiumBy.XPATH,
            "//android.widget.CheckedTextView[@resource-id='com.babysoft.ecommerce_demo:id/design_menu_item_text' and @text='My Account']",
        )

        # Create ActionChains instance and pass the driver
        action = ActionChains(self.driver)

        # Move to the element and click it
        action.move_to_element(My_account).click().perform()
        time.sleep(10)

        sign_up = self.driver.find_element(
            AppiumBy.ID, "com.babysoft.ecommerce_demo:id/btn_signup"
        )

        # Click the sign-up button using ActionChains
        action.click(sign_up).perform()
