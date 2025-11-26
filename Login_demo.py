from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Initialize driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open site
driver.get("https://brioanalytics.ai/")

wait = WebDriverWait(driver, 10)

# Login button
wait.until(EC.element_to_be_clickable((By.ID, "login-button_"))).click()

# Username & Password (placeholder values)
username = os.getenv("BRIO_USERNAME")  # Stored securely
password = os.getenv("BRIO_PASSWORD")

wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(username)
wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))).click()

# Example clickable card (cleaned XPATH)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "(//div[@class='mb-md-3 col-lg-3 col-md-4 col-sm-12'])[2]")
)).click()

driver.quit()