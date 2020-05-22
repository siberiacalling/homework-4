import os
import warnings
from unittest import TestCase

from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseTest(TestCase):
    driver: Remote

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        try:
            self.before_each()
        except:
            self.tearDown()

    def before_each(self):
        pass

    def after_each(self):
        pass

    def tearDown(self):
        try:
            self.after_each()
        finally:
            self.driver.quit()
