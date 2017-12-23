import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('../../Test/drivers/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url, desired_capabilities=webdriver.DesiredCapabilities.CHROME)
driver.get('http://www.google.com/xhtml')
service.stop()
time.sleep(5) # Let the user actually see something!
driver.quit()