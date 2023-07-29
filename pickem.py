import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
UNDERDOG="https://underdogfantasy.com/login"
PRIZEPICKS="https://api.prizepicks.com/projections"

class Player:
    def __init__(self, id, name, team, )

# service = ChromeService(executable_path=PATH)
driver = webdriver.Chrome()
driver.get(PRIZEPICKS)
time.sleep(5)
driver.maximize_window()

json_content = json.loads(driver.find_element(By.CSS_SELECTOR, 'body > pre').text)

players = json_content['included']
data = json_content['data']
playerDict = {}
for player in players:
    playerDict[player['id']] = player['attributes']['name']

for i in playerDict:
    print(i) 
# elements = driver.find_elements(By.TAG_NAME, "input")


# for e in elements:
#     print(e)
# uname = elements[0]
# ActionChains(driver)\
# .move_to_element(uname)\
# .pause(1)\
# .send_keys("joebruin@gmail.com\t")\
# .pause(1)\
# .send_keys("!Nsert123\t\t\t")\
# .perform()

# time.sleep(3)

# signIn = driver.switch_to.active_element
# signIn.click()

# time.sleep(3)
# driver.switch_to.active_element

# ActionChains(driver).send_keys("\t\t").perform()
# driver.switch_to.active_element.click()

# cards = driver.find_elements(By.CLASS_NAME, "styles__overUnderCell__KgzNn")

# for card in cards:
#     name = card.find_element(By.CSS_SELECTOR, "styles__playerName__jW6mb").text()
#     print(name)


time.sleep(50) 
