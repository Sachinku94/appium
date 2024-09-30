
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService

import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
import time
@pytest.fixture(scope="class")
def setup(request):

    global appium_service
    appium_service= AppiumService()
    appium_service.start()
    global driver

    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': "uiautomator2",
        'deviceName': 'emulator-5554',
        'appPackage': 'com.android.chrome',
        'appActivity': 'com.google.android.apps.chrome.Main',
        'language': 'en',
        'locale': 'US'
    }

    url = 'http://localhost:4723'

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    
    request.cls.driver = driver
    yield
    print("closing teardown_function")
    driver.quit()
    appium_service.stop()