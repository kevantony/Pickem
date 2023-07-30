import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
UNDERDOG="https://underdogfantasy.com/login"
PRIZEPICKSPROJECTIONS="https://api.prizepicks.com/projections"
PRIZEPICKSLEAGUES="https://api.prizepicks.com/leagues"

class Player:
    def __init__(self, name, sport, team, line = "", stat_type = ""):
        self.name=name
        self.sport=sport
        self.team=team
        self.line=line
        self.stat_type=stat_type

# service = ChromeService(executable_path=PATH)
driver = webdriver.Chrome()
# driver.get(PRIZEPICKSPROJECTIONS)
# time.sleep(5)
# driver.maximize_window()
# projections = json.loads(driver.find_element(By.CSS_SELECTOR, 'body > pre').text)



# players = projections['included']
# data = projections['data']
# playerDict = {}
# PrizepicksPlayers = {}
# for player in players:
#     attr = player['attributes']
#     if (len(attr)) != 8:
#         continue
#     playerDict[player['id']] = [attr['name'], attr['league'], attr['team']]


# for entry in data:
#     id = entry['relationships']['new_player']['data']['id']
#     playerInfo = playerDict[id]
#     name=playerInfo[0]
#     sport=playerInfo[1]
#     team=playerInfo[2]
#     line=entry['attributes']['line_score']
#     stat=entry['attributes']['stat_type']
#     PrizepicksPlayers[id] = Player(name,sport, team,line, stat)

# for val in PrizepicksPlayers.values():
#     print(val.__dict__)



driver.get(UNDERDOG)
time.sleep(5)

elements = driver.find_elements(By.TAG_NAME, "input")


for e in elements:
    print(e)
uname = elements[0]
ActionChains(driver)\
.move_to_element(uname)\
.pause(1)\
.send_keys("joebruin0335@gmail.com\t")\
.pause(1)\
.send_keys("!Nsert123\t\t\t")\
.perform()

time.sleep(3)

signIn = driver.switch_to.active_element
signIn.click()

time.sleep(3)

driver.get(UNDERDOG)
# driver.switch_to.active_element

# ActionChains(driver).send_keys("\t\t").perform()
# driver.switch_to.active_element.click()

# cards = driver.find_elements(By.CLASS_NAME, "styles__overUnderCell__KgzNn")

# for card in cards:
#     name = card.find_element(By.CSS_SELECTOR, "styles__playerName__jW6mb").text()
#     print(name)


time.sleep(50) 
