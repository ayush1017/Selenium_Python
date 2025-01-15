from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os


# Force the latest driver version to match Chrome version 131
logging.basicConfig(filename="automation_log.txt", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

#making folder to save the screenshots
folder_name="ScreenShots_"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Function to take a screenshot and save it
def take_screenshot(step_name):
    screenshot_filename =os.path.join(folder_name,f"screenshot_{step_name}.png") 
    driver.save_screenshot(screenshot_filename)
    logger.info(f"Screenshot saved as {screenshot_filename}")
    
service=Service('chromedriver.exe')
driver = webdriver.Chrome(
    service=service
)
  # Ensure the ChromeDriver is in PATH.
wait = WebDriverWait(driver, 10)


# Force the latest driver version to match Chrome version 131
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Navigate to the website
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    print("Website loaded successfully.")
    logger.info("Website loaded successfully.")
    time.sleep(3)
    take_screenshot("navigate_to_website")

    # Step 2: Verify Page Title
    page_title = driver.title
    print(f"Page Title: {page_title}")
    assert "Swag Labs" in page_title, "Page title does not match!"
    logger.info(f"Page Title: {page_title}")
    time.sleep(3)
    take_screenshot("verify_page_title")

    # Step 3: Enter username
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")
    print("Entered username.")
    logger.info("Entered username: standard_user.")
    time.sleep(3)
    take_screenshot("enter_username")

    # Step 4: Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    print("Entered password.")
    logger.info("Entered password: secret_sauce.")
    time.sleep(3)
    take_screenshot("enter_password")

    # Step 5: Click the "Login" button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    print("Logged in successfully.")
    logger.info("Logged in successfully.")
    time.sleep(3)
    take_screenshot("click_login")

    # Step 6: Add to Cart for the third product
    add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
    add_to_cart_buttons[2].click()  # Index 2 for the third product
    print("Added the third product to the cart.")
    logger.info("Added the third product to the cart.")
    time.sleep(3)
    take_screenshot("add_to_cart")

    # Step 7: Click the cart icon
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    print("Navigated to the cart.")
    logger.info("Navigated to the cart.")
    time.sleep(3)
    take_screenshot("click_cart_icon")

    # Step 8: Verify product is added to the cart
    cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
    assert len(cart_items) == 1, "Product not added to the cart!"
    print("Verified the product is added to the cart.")
    logger.info("Verified the product is added to the cart.")
    time.sleep(3)
    take_screenshot("verify_product_in_cart")

    # Step 9: Click the "Checkout" button
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    print("Clicked on the Checkout button.")
    logger.info("Clicked on the Checkout button.")
    time.sleep(3)
    take_screenshot("click_checkout")

    # Step 10: Fill out the checkout form
    first_name_field = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    first_name_field.send_keys("Test")
    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("User")
    zip_code_field = driver.find_element(By.ID, "postal-code")
    zip_code_field.send_keys("12345")
    print("Filled out the checkout form.")
    logger.info("Filled out the checkout form.")
    time.sleep(3)
    take_screenshot("fill_checkout_form")

    # Step 11: Click "Continue"
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    print("Clicked Continue.")
    logger.info("Clicked Continue.")
    time.sleep(3)
    take_screenshot("click_continue")

    # Step 12: Click "Finish" button
    finish_button = wait.until(EC.presence_of_element_located((By.ID, "finish")))
    finish_button.click()
    print("Order completed successfully.")
    logger.info("Order completed successfully.")
    time.sleep(3)
    take_screenshot("click_finish")

    # Step 13: Verify the order success message
    success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    print("Verified the order success message: THANK YOU FOR YOUR ORDER.")
    logger.info("Verified the order success message: THANK YOU FOR YOUR ORDER.")

finally:
    # Close the browser after a short delay
    time.sleep(2)
    driver.quit()
    print("Browser closed.")
    logger.info("Browser closed.")
   