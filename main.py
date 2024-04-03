from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import keyboard
from selenium.webdriver.common.keys import Keys


# Configurations
login_time = 20  # Time for login (in seconds)
new_msg_time = 5  # Time for a new message (in seconds)
send_msg_time = 5  # Time for sending a message (in seconds)
country_code = 92  # Set your country code
action_time = 2  # Set time for button click action

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
text = "automate texting with python chatbot"

# Open browser with default link
link = "https://web.whatsapp.com"
driver.get(link)
time.sleep(login_time)




# Loop Through Numbers List
with open("numbers.txt", "r") as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f"https://web.whatsapp.com/send/?phone={country_code}{num}"
        driver.get(link)
        time.sleep(new_msg_time)
        # time.sleep(new_msg_time)
        element = WebDriverWait(driver, 20).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, "._ak1l .xh8yej3 .x1hx0egp p.selectable-text.copyable-text.x15bjb6t.x1n2onr6"))
)
   
        element.click()  
        time.sleep(new_msg_time)
        
        for char in text:
            keyboard.write(char,delay=0)
              
        keyboard.press_and_release('enter')
        time.sleep(new_msg_time)
        

# Quit the driver
driver.quit()
