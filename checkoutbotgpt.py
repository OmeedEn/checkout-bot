from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the webdriver (make sure the correct driver for your browser is installed)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the website
driver.get("https://www.example.com")

try:
    # Log in to the website
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    username.send_keys("your_username")
    password.send_keys("your_password")
    password.send_keys(Keys.RETURN)

    # Wait for login to complete
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Account']"))
    )

    # Navigate to the product page
    driver.get("https://www.example.com/product-page")

    # Add the product to the cart
    add_to_cart_button = driver.find_element(
        By.XPATH, "//button[text()='Add to Cart']")
    add_to_cart_button.click()

    # Go to the checkout page
    driver.get("https://www.example.com/cart")

    checkout_button = driver.find_element(
        By.XPATH, "//button[text()='Checkout']")
    checkout_button.click()

    # Fill out checkout form
    # Adjust the element selectors based on the website's checkout form
    first_name = driver.find_element(By.NAME, "firstName")
    last_name = driver.find_element(By.NAME, "lastName")
    address = driver.find_element(By.NAME, "address")
    city = driver.find_element(By.NAME, "city")
    state = driver.find_element(By.NAME, "state")
    zip_code = driver.find_element(By.NAME, "zipCode")
    credit_card = driver.find_element(By.NAME, "creditCard")

    first_name.send_keys("John")
    last_name.send_keys("Doe")
    address.send_keys("123 Main St")
    city.send_keys("Anytown")
    state.send_keys("CA")
    zip_code.send_keys("12345")
    credit_card.send_keys("4111111111111111")

    # Submit the order
    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Place Order']")
    submit_button.click()

    # Wait for order confirmation
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[text()='Order Confirmation']"))
    )

    print("Order placed successfully!")

finally:
    # Close the browser
    driver.quit()
