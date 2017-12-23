import unittest
from selenium import webdriver
import selenium.webdriver.chrome.service as ser
import os

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
        if "Test" in str(os.getcwd()):
            pathchrome = os.path.abspath(os.path.join(os.pardir, 'drivers/chromedriver.exe'))
            # print(pathchrome)
        else:
            pathchrome = os.path.abspath(os.path.join(os.getcwd(), 'Test', 'drivers', 'chromedriver.exe'))

        self.servce = ser.Service(pathchrome)
        self.servce.start()
        self.driver = webdriver.Remote(command_executor=self.servce.service_url, desired_capabilities=webdriver.DesiredCapabilities.CHROME)
        # self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME, command_executor='http://127.0.0.1:4444/wd/hub')
        # self.driver = webdriver.Chrome("Test/drivers/chromedriver.exe")
        self.driver.get("https://www.google.co.in/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        """[summary]
        tearDown method closes all the browser instances and then quit.
        """
        # with allure.step("Close browser"):

        if self.driver is not None:
            self.driver.close()





