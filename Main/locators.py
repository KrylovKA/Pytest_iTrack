from selenium.webdriver.common.by import By

class Authentication (object):
    login = (By.XPATH, "//input[@name='login']")
    password = (By.XPATH, "//input[@name='password']")