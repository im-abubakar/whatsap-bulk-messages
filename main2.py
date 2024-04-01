# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Config
login_time = 80                 # Time for login (in seconds)
new_msg_time = 20               # Time for a new message (in seconds)
send_msg_time = 20              # Time for sending a message (in seconds)
country_code = 92               # Set your country code
action_time = 2                 # Set time for button click action

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text
with open('message.txt', 'r') as file:
    msg = file.read()

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# List of contact names from EMS1 to EMS50
contact_names = [f"EMS{i}" for i in range(1, 3)]

# Loop Through Contact Names
for contact_name in contact_names:
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact_name)
    time.sleep(2)  # Wait for contact to appear in search results
    # Click on the contact to open the chat
    contact = driver.find_element_by_xpath(f'//span[@title="{contact_name}"]')
    contact.click()
    time.sleep(new_msg_time)
    # Start the action chain to write the message
    actions = ActionChains(driver)
    for line in msg.split('\n'):
        actions.send_keys(line)
        # SHIFT + ENTER to create next line
        actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(send_msg_time)

# Quit the driver
driver.quit()
