import unittest
import time
import allure
from selenium import webdriver


class EnvSetup(unittest.TestCase):
    """[summary]
    EnvSetup class is used to setup during start of testcase and stop of test case.
    [description]
    """
    def setUp(self):
        """[summary]
        setUp contains browser setup attributes.
        [description]
        """
        # Control cockpit launch
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.co.in/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        """[summary]
        tearDown method closes all the browser instances and then quit.
        """
        with allure.step("Close browser"):
            if self.driver is not None:
                self.driver.close()
                if self.driver is not None:
                    self.driver.quit()




