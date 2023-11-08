from selenium import webdriver # import webdriver
from selenium.webdriver.common.by import By  # Import the By class
import os # geckodriver was not opening so this was the hotfix
from selenium.webdriver.support.ui import WebDriverWait # wait library
from selenium.webdriver.support import expected_conditions as EC # conditions library
from selenium.webdriver.support.ui import Select # select dropdown menus
from selenium.webdriver.firefox.options import Options # make firefox hidden

# Set the path to GeckoDriver
PATH_TO_GECKODRIVER = 'gecko/geckodriver'  # Replace with the actual path

# Set GeckoDriver path as an environment variable
os.environ['PATH'] += ':' + PATH_TO_GECKODRIVER

# To open firefox in headless
firefox_options = Options()
firefox_options.headless = True
driver = webdriver.Firefox(options=firefox_options)

# enable this below and comment upper three lines to make firefox appear
#driver = webdriver.Firefox()


#acess webpage
driver.get("http://192.168.0.60:8096/web/index.html#!/configurationpage?name=Ani-Sync")

# enter the login fields
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "txtManualName"))
)
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "txtManualPassword"))
)
username_field.send_keys("rodhfr")
password_field.send_keys("ni140817")


sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign In')]"))
)
sign_in_button.click()


# Navigate to Ani-sync settings
span_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='material-icons person']"))
)
span_element.click()

dashboard_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='listItemBodyText' and contains(text(), 'Dashboard')]"))
)
dashboard_element.click()

plugins_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'navMenuOption') and .//span[@class='navMenuOptionText' and contains(text(), 'Plugins')]]"))
)
plugins_link.click()

ani_sync_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.cardImageContainer[href*='configurationpage?name=Ani-Sync']"))
)
ani_sync_link.click()


# Scroll down page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Update provider with Jellyfin progress
select_action = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "selectAction"))
)

select = Select(select_action)

select.select_by_visible_text("Update provider with Jellyfin progress")



# Select user 
select_user = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "selectSyncUser"))
)

select = Select(select_user)

select.select_by_visible_text("rodhfr")

# Find and click the "Run" button
run_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "run"))
)
run_button.click()

# quit browser
driver.quit()