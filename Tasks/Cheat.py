from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Use and install a chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL of the game
driver.get("https://studio.code.org/projects/applab/BPizZMXpqHSfkO8IUWCTgEH52_hlwH8FM_jXXpOwhK4")

# Waiting for page content to be loaded.
time.sleep(1)

# Start game
start = driver.find_element_by_id( 'start' )
start.click()

# Get the element
button = driver.find_element_by_id( 'button1' )

# Create loop
for i in range(0,9999999999):
	# Click the button
	button.click()

	# Preventing the script to crash
	time.sleep(0.00005)

	# Find the button once again, since it gets reloaded.
	button = driver.find_element_by_id( 'button1' )
