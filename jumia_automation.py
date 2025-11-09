from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    # --- Step 1: Launch Chrome ---
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)  # waits for elements up to 10 seconds

    # --- Step 2: Go to Jumia ---
    driver.get("https://www.jumia.com.ng/")
    print("🌍 Jumia homepage opened.")
    time.sleep(3)

    # --- Step 3: Login to Jumia ---
    print("🔑 Logging into Jumia...")

    # Click the Account icon
    account_icon = driver.find_element(By.XPATH, '//a[@aria-label="Account" or contains(@href,"customer/account")]')
    account_icon.click()
    time.sleep(2)

    # Click "Sign In"
    sign_in_link = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In") or contains(text(),"Login")]')
    sign_in_link.click()
    time.sleep(3)

    # Enter your email
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("YOUR_EMAIL_HERE")  # 🔒 Replace with your Jumia email
    email_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Enter your password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("YOUR_PASSWORD_HERE")  # 🔒 Replace with your Jumia password
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    print("✅ Login successful (if credentials are correct).")

    # --- Step 4: Search for a Product ---
    print("🔍 Searching for product...")
    search_box = driver.find_element(By.XPATH, '//input[@type="text" and @name="q"]')
    search_box.send_keys("wireless mouse")  # 🖱️ Change to any product you want
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    # --- Step 5: Select the First Product ---
    print("🛒 Selecting the first product...")
    first_product = driver.find_element(By.XPATH, '(//a[contains(@class,"core")])[1]')
    first_product.click()
    time.sleep(5)

    # Switch to new tab (Jumia opens product in a new tab)
    driver.switch_to.window(driver.window_handles[1])

    # --- Step 6: Add to Cart ---
    print("📦 Adding product to cart...")
    add_to_cart_button = driver.find_element(By.XPATH, '//button[contains(text(),"Add to cart")]')
    add_to_cart_button.click()
    time.sleep(5)

    # --- Step 7: Go to Cart ---
    print("🧾 Going to cart...")
    cart_button = driver.find_element(By.XPATH, '//a[contains(text(),"Cart")]')
    cart_button.click()
    time.sleep(5)

    # --- Step 8: Proceed to Checkout ---
    print("💳 Proceeding to checkout...")
    proceed_button = driver.find_element(By.XPATH, '//a[contains(text(),"CHECKOUT")]')
    proceed_button.click()
    time.sleep(5)

    print("✅ Automation complete — checkout page reached!")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    input("\nPress Enter to close the browser...")
    driver.quit()