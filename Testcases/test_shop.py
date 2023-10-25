import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.shopPage import ShopPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_shop:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_shop(self):
        self.logger.info("   Test_002_Shop")
        self.logger.info("   Launching Browser")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.sp = ShopPage(self.driver)
        self.logger.info("   Searching for carting item")
        self.sp.clickSearchbox("ber")
        self.sp.searchboxEnterkey_xpath()
        results = self.sp.getItemNames()
        self.expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
        self.actualList = []
        count = len(results)
        assert count > 0
        for result in results:
            self.actualList.append(result.find_element(By.XPATH, "h4").text)
            result.find_element(By.XPATH, "div/button").click()
        assert self.expectedList == self.actualList

        self.logger.info("   Added item(s) to Cart")
        self.sp.clickImageCart()
        self.sp.clickCheckout()
        self.logger.info("  Checkout Procedure Has been started")
        self.sp.enterPromocode("rahulshettyacademy")
        self.sp.ApplyPromocode()
        self.sp.clickPlaceOrder()
        self.logger.info("   Order placement has been initialized")
        self.sp.enterCountryName("India")
        self.sp.clickCheckbox()
        self.sp.clickProceed()
        self.logger.info("   Order has been Placed")
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        if 'Success! Thank you! Your order will be delivered in next few weeks :-).' in textMatch:
            assert True
            self.logger.info("   Successfully Completed Purchasing")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_shop_scr.png")
            self.logger.error("   Test Unsuccessful")
            assert False
