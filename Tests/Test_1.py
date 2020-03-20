import unittest
from selenium import webdriver
from time import localtime, strftime, sleep
from selenium.webdriver.common.by import By

# opts = Options()
# opts.set_headless()
# assert opts.headless  # без графического интерфейса.
#
# browser = Firefox(options=opts)
# browser.get('https://duckduckgo.com')


class TraceWay(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://itrack.demo.dev-og.com/')

    def test_01(self):
        driver = self.driver
        sleep(1)
        input_field_login = driver.find_element(By.XPATH, "//input[@name='login']")
        input_field_login.send_keys("root")
        input_field_password = driver.find_element(By.XPATH, "//input[@name='password']")
        input_field_password.send_keys("123123")
        sleep(1)
        python_button = driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
        python_button.click()
        sleep(1)
        assert "TraceWay" in driver.page_source
        driver.quit()

# class Google(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get('http://google.com')
#
#     def test_01(self):
#         driver = self.driver.find_elements_by_class_name("gLFyf gsfi")
#         sleep(1)
#         input_field = driver.f
#         input_field_login.send_keys("root")
#         driver.quit()