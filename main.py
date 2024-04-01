from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurations
login_time = 30                # Time for login (in seconds)
new_msg_time = 5              # Time for a new message (in seconds)
send_msg_time = 5             # Time for sending a message (in seconds)
country_code = 92              # Set your country code
action_time = 2                # Set time for button click action
image_path = "D:\\message_send\\whatsapp-bulk-messenger\\image.png"  # Absolute path to your image

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def send_message(message):
    input_box = driver.find_element_by_css_selector('div[data-tab="6"]')
    input_box.send_keys(message)
    input_box.send_keys(Keys.ENTER)


# Encode Message Text
with open("message.txt", "r") as file:
    msg = file.read()

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
        print("link is ", link)
        print(msg)
        time.sleep(new_msg_time)
        
        # text = "To type text here"
        # i think issue is in this loop
        for line in msg:
            actions = ActionChains(driver)
            actions.send_keys(line)
            print("this",line)
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(send_msg_time)

# Quit the driver
driver.quit()
