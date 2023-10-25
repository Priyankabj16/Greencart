import pytest
import faulthandler
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_HomePageTitle:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepageTitle(self):
        self.logger.info("   Test_001_HomePageTitle")
        self.logger.info("   Launching Browser")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.exp_title = "GreenKart - veg and fruits kart"
        if self.driver.title == self.exp_title:
            assert True
            self.logger.info("   Test Successful")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle_scr.png")
            self.logger.error("   Test Unsuccessful")
            assert False
