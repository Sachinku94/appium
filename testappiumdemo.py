# from appium.webdriver.common.appiumby import AppiumBy
# from utilities.base_class import BaseClass
# import pytest
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException


# @pytest.mark.usefixtures("setup")  # Apply the setup fixture to this test class
# class Testone(BaseClass):

#     def test_demoapp(self):
#         time.sleep(20)
#         wait = WebDriverWait(
#             self.driver, 30, poll_frequency=5, ignored_exceptions=[TimeoutException]
#         )
#         self.driver.find_element(
#             AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer"
#         ).click()
#         time.sleep(20)

#         all_selected = (
#             AppiumBy.CLASS_NAME,
#             "a.b.h.h.la",
#         )
#         while True:
#             all_select = wait.until(EC.visibility_of_all_elements_located(all_selected))

#             try:
#                 for select in all_select:

#                     # print(len(all_select))
#                     # for select in all_select:

#                     select.click()
#                     time.sleep(5)
#                     home = self.driver.find_element(
#                         AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer"
#                     )

#                     try:
#                         if home.is_displayed:
#                             home.click()
#                             time.sleep(20)
#                         else:
#                             back = self.driver.find_element(
#                                 AppiumBy.ACCESSIBILITY_ID, "Navigate up"
#                             )

#                             back.click()
#                             time.sleep(5)
#                             home.click()

#                     except Exception:
#                         ()
#             except Exception:
#                 ()


from appium.webdriver.common.appiumby import AppiumBy
from utilities.base_class import BaseClass
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.mark.usefixtures("setup")  # Apply the setup fixture to this test class
class Testone(BaseClass):

    def test_demoapp(self):
        time.sleep(20)
        wait = WebDriverWait(
            self.driver, 30, poll_frequency=5, ignored_exceptions=[TimeoutException]
        )
        self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer"
        ).click()
        time.sleep(20)

        all_selected = (
            AppiumBy.CLASS_NAME,
            "a.b.h.h.la",
        )

        while True:
            try:
                all_select = wait.until(
                    EC.visibility_of_all_elements_located(all_selected)
                )

                if not all_select:
                    break  # Exit loop if no more elements found

                for select in all_select:
                    select.click()
                    time.sleep(5)

                    home = self.driver.find_element(
                        AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer"
                    )

                    if home.is_displayed():
                        home.click()
                        time.sleep(20)
                    else:
                        back = self.driver.find_element(
                            AppiumBy.ACCESSIBILITY_ID, "Navigate up"
                        )
                        back.click()
                        time.sleep(5)
                        home.click()

                # Refresh the list of elements after processing one round
                all_select = wait.until(
                    EC.visibility_of_all_elements_located(all_selected)
                )

            except Exception as e:
                print(f"An error occurred: {e}")
                break
