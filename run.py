from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

# URL of the Selenium Grid or remote WebDriver server
selenium_server_url = "http://13.126.89.154:4444/wd/hub"

# Configure Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
print("Connecting to remote Selenium WebDriver...")
driver = webdriver.Remote(
    command_executor=selenium_server_url,
    options=options
)

try:
    # Step 1: Navigate to the application URL
    app_url = os.getenv("ENDPOINT_URL", "http://your-application-url.com")
    print(f"Navigating to application URL: {app_url}")
    driver.get(app_url)

    # Step 2: Perform actions
    print("Performing actions on the application...")
    search_box = driver.find_element(By.NAME, "q")  # Locate the search box
    print("Located search box, entering search term...")
    search_box.send_keys("test query" + Keys.RETURN)  # Enter search term and submit
    print("Search term submitted.")

    # Step 3: Wait for the results to load
    wait_time = 5
    print(f"Waiting for {wait_time} seconds for the results to load...")
    time.sleep(wait_time)

    # Step 4: Verify the result
    print("Verifying the search results...")
    results = driver.find_elements(By.CSS_SELECTOR, "h3")  # Locate results by CSS selector
    assert len(results) > 0, "No results found"
    print("Test passed: Search results found")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Step 5: Close the browser
    print("Closing the browser...")
    driver.quit()
    print("Browser closed.")
