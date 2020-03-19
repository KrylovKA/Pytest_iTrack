from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()
assert opts.headless  # без графического интерфейса.

browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')


class TraceWay(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://itrack.demo.dev-og.com/')
        sleep(1)
        assert "TraceWay" in driver.page_source
        driver.quit()