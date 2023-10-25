from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ShopPage:
    searchbox_css = ".search-keyword"
    searchboxEnterkey_xpath = "//button[@type='submit']"
    itemsNames_xpath = "//div[@class='products']/div"
    imageCart_css = "img[alt='Cart']"
    checkout_xpath = "//button[text()='PROCEED TO CHECKOUT']"
    promoCode_css = ".promoCode"
    applyPromocode_css = ".promoBtn"
    placeOrder_xpath = "//button[normalize-space()='Place Order']"
    countryName_xpath = "//div[@class='wrapperTwo']//div//select"
    checkbox_xpath = "//input[@type='checkbox']"
    btnProceed_xpath = "//button[normalize-space()='Proceed']"

    def __init__(self, driver):
        self.driver = driver

    def clickSearchbox(self, iname):
        self.driver.find_element(By.CSS_SELECTOR, self.searchbox_css).send_keys(iname)

    def SearchboxEnterkey(self):
        self.driver.find_element(By.XPATH, self.searchboxEnterkey_xpath).click()

    def getItemNames(self):
        self.driver.find_element(By.XPATH, self.itemsNames_xpath)

    def clickImageCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.imageCart_css).click()

    def clickCheckout(self):
        self.driver.find_element(By.XPATH, self.checkbox_xpath).click()

    def enterPromocode(self, pcName):
        self.driver.find_element(By.CSS_SELECTOR, self.promoCode_css).send_keys(pcName)

    def ApplyPromocode(self):
        self.driver.find_element(By.CSS_SELECTOR, self.applyPromocode_css).click()

    def clickPlaceOrder(self):
        self.driver.find_element(By.XPATH, self.placeOrder_xpath).click()

    def enterCountryName(self, Cname):
        drp = Select(self.driver.find_element(By.XPATH, self.countryName_xpath))
        drp.select_by_visible_text(Cname)

    def clickCheckbox(self):
        self.driver.find_element(By.XPATH, self.checkbox_xpath).click()

    def clickProceed(self):
        self.driver.find_element(By.XPATH, self.btnProceed_xpath).click()
