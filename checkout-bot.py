import time
import account
import pickle
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CheckOutBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=/home/mike/chrome-checkout")
        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.opentable.com/")

    def __del__(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

    def accept_cookies(self):
        button = self.driver.find_element(
            By.ID, "privacy-layer-accept-all-button")
        button.click()

    def login(self, email, password, phone_number):
        sign_in = self.driver.find_element(
            By.XPATH, '//button[@data-test="header-sign-in-button"]')
        sign_in.click()

        time.sleep(5)
        # email_input = self.driver.find_element(By.ID, "mms-login-form__email")
        # email_input.clear()
        # email_input.send_keys(email)
        # pass_input = self.driver.find_element(By.ID, "mms-login-form__password")
        # pass_input.clear()
        # pass_input.send_keys(password)
        phone_input = self.driver.find_element(By.ID, "phoneNumber")
        phone_input.clear()
        phone_input.send_keys(phone_number)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button.MSzY1aFyA5I-.VVTDKCFa1Lg-.H-HxM96BggY-._3pWpWi7I-U8-.YgjZmsoa-Gk-[aria-disabled="false"][data-test="continue-button"]').click()
        time.sleep(3)

    def reserve_table(self, link):
        self.driver.get(link)
        time.sleep(1)
        reserve_button = self.driver.find_element(
            By.CSS_SELECTOR, "a[href*='d=2024-05-24T18%3A00%3A00']")
        reserve_button.click()
        time.sleep(2)

    def complete_reservation(self, link):
        self.driver.get(link)
        time.sleep(1)
        complete_button = self.driver.find_element(
            By.ID, "complete-reservation")
        complete_button.click()
        time.sleep(2)

    def add_product_to_cart(self, link):
        self.driver.get(link)
        time.sleep(1)
        add_to_cart_button = self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="a2c-Button"]')
        add_to_cart_button.click()
        time.sleep(2)

    def checkout(self):
        self.driver.get("https://www.mediamarkt.de/checkout/payment")
        time.sleep(1)
        self.driver.find_elements(
            By.CLASS_NAME, "SelectGroupstyled__SelectGroupItemContainer-sc-1iooaif-0")[2].click()
        time.sleep(1)
        self.driver.find_elements(
            By.CLASS_NAME, "ContinueButton__StyledContinue-fh9abp-0")[1].click()

        # this is how you click the final checkout button
        # self.driver.find_elements(By.CLASS_NAME, "ContinueButton__StyledContinue-fh9abp-0")[1].click()


if __name__ == "__main__":
    checkout_bot = CheckOutBot()

    checkout_bot.driver.get("https://www.opentable.com/")

    # checkout_bot.login(account.email, account.password)
    # time.sleep(30)
    # exit()

    # checkout_bot.login(account.email, account.password, account.phone_number)
    checkout_bot.reserve_table("https://www.opentable.com/")
    checkout_bot.complete_reservation("https://www.opentable.com/booking/details?availabilityToken=eyJ2IjoyLCJtIjowLCJwIjowLCJjIjoxODQ2ODE2LCJzIjowLCJuIjowfQ&correlationId=4c48dde4-22c9-4c48-be5b-32ed6369f016&creditCardRequired=false&dateTime=2024-05-24T18%3A00%3A00&partySize=2&points=100&pointsType=Standard&resoAttribute=default&rid=3287&slotHash=2622637950&isModify=false&isMandatory=false&cfe=true")

    # checkout_bot.add_product_to_cart("https://www.mediamarkt.de/de/product/_sandisk-extreme%C2%AE-2484123.html")
    # checkout_bot.checkout()
    time.sleep(20)
