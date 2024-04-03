from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


# Configurations
login_time = 30  # Time for login (in seconds)
new_msg_time = 5  # Time for a new message (in seconds)
send_msg_time = 5  # Time for sending a message (in seconds)
country_code = 92  # Set your country code
action_time = 2  # Set time for button click action

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open browser with default link
link = "https://web.whatsapp.com"
driver.get(link)
time.sleep(login_time)

text = "To type text here"
# Loop Through Numbers List
with open("numbers.txt", "r") as file:
    for num in file.readlines():
        num = num.strip()
        link = f"https://web.whatsapp.com/send/?phone={country_code}{num}"
        driver.get(link)
        time.sleep(new_msg_time)
        
        # Find the input element
        input_box = driver.find_element(By.CSS_SELECTOR, ".x6ikm8r")
        
        for char in text:
            input_box.send_keys(char)
        time.sleep(new_msg_time)
        input_box.send_keys(Keys.ENTER)
        
        
            
        
        
   
        
        # Send the message
        send_button = driver.find_element(By.CSS_SELECTOR, ".x1c4vz4f")
        
        send_button.click()
        
        time.sleep(send_msg_time)

# Quit the driver
driver.quit()
