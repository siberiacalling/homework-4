import os
from unittest import TestCase

from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test(TestCase):
    driver: Remote

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        raise NotImplementedError(f'test() not implemented in {self.__class__.__name__}')
