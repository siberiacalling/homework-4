import os
import warnings
from unittest import TestCase

from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test(TestCase):
    driver: Remote

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()
