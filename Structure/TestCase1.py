import time

from selenium.webdriver import Keys

from Structure.Base import EnvironmentSetup
from Structure.PageObjectModel import Locator

from selenium.webdriver.common.by import By

Loc = Locator()


class Home(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://www.google.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        driver.find_element(By.XPATH, Loc.text).send_keys('kabir', Keys.ENTER)
        time.sleep(10)