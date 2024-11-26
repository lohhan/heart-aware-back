from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver (ensure that the correct WebDriver is installed)
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed

def test_form_submission():
    try:
        # Open the form URL
        driver.get("http://localhost:5173")  # Replace with your actual URL
        
        # Wait until the form is visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form"))
        )

        # Fill in the form
        driver.find_element(By.CSS_SELECTOR, 'input[ref="inputAge"]').send_keys("45")
        driver.find_element(By.CSS_SELECTOR, 'select[ref="inputGen"]').send_keys("1")  # Masculine
        driver.find_element(By.CSS_SELECTOR, 'select[ref="inputAg"]').send_keys("1")  # Yes
        driver.find_element(By.CSS_SELECTOR, 'select[ref="inputVasos"]').send_keys("2")
        driver.find_element(By.CSS_SELECTOR, 'select[ref="inputPain"]').send_keys("0")  # Typical Angina
        driver.find_element(By.CSS_SELECTOR, 'input[ref="inputPress"]').send_keys("120")
        driver.find_element(By.CSS_SELECTOR, 'input[ref="inputColes"]').send_keys("200")
        driver.find_element(By.CSS_SELECTOR, 'select[ref="inputSugar"]').send_keys("1")  # Yes
        driver.find_element(By.CSS_SELECTOR, 'select[ref="inputEletro"]').send_keys("0")  # Normal
        driver.find_element(By.CSS_SELECTOR, 'input[ref="inputFreq"]').send_keys("180")
        
        # Click the 'Generate results' button
        driver.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()

        # Wait for the modal to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ReactModal__Content"))
        )

        # Check the modal content
        modal_content = driver.find_element(By.CSS_SELECTOR, ".ReactModal__Content")
        assert "Attention: Risk of Heart Problems Detected" in modal_content.text or "Everything is fine with your cardiovascular health!" in modal_content.text

        # Close the modal
        driver.find_element(By.CSS_SELECTOR, '.botaofechar').click()
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        time.sleep(3)  # Give some time to observe the result

test_form_submission()
