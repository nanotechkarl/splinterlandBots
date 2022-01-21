from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

USERNAME = os.getenv("User_name")
POSTINGKEY = os.getenv("Posting_key")



# Chrome required
driver = webdriver.Chrome()
driver.get('https://splinterlands.com/?p=battle_history')

try:
    RANGE = int(os.getenv("Battles_To_Surrender"))
except ValueError:
    print('******** Please Enter Valid number in .env then run "python auto-surrender.py" again ********')
    driver.quit()
    exit()

loginButton = driver.find_element_by_xpath('//*[@id="log_in_button"]/button')
loginButton.click()

driver.implicitly_wait(10)
inputUsername = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
inputUsername.send_keys(USERNAME)

driver.implicitly_wait(10)
inputPassword = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
inputPassword.send_keys(POSTINGKEY)


if USERNAME and POSTINGKEY:
    loginCredentials = driver.find_element_by_xpath(' //*[@id="loginBtn"]')
    loginCredentials.click()


# force sleep 
####### you can costumize time.sleep(10) depending on how long until the announcement tab shows. for this 10 seconds ######## 
time.sleep(10)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

goToBattleTab = driver.find_element_by_xpath('//*[@id="menu_item_battle"]/a')
goToBattleTab.click()


# loop1 here #
for a in range(RANGE):
    time.sleep(3)
    battle = driver.find_element_by_xpath('//*[@id="battle_category_btn"]')
    battle.click()

    time.sleep(3)
    createTeam = driver.find_element_by_xpath('//*[@id="dialog_container"]/div/div/div/div[2]/div[3]/div[2]/button')
    createTeam.click()

    time.sleep(3)
    summoner = driver.find_element_by_xpath("//*[contains(@id, 'starter-167')]")
    summoner.click()

    time.sleep(1)
    monster = driver.find_element_by_xpath("//*[contains(@id, 'starter-157')]")
    monster.click()

    time.sleep(3)
    fight = driver.find_element_by_xpath('//*[@id="page_container"]/div/div[1]/div/button')
    fight.click()

    skipBattle = WebDriverWait(driver, 210).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="btnSkip"]')))
    time.sleep(5)
    skipBattle.click()

    #! if enemy surrendered wait for atleast 4 minutes till it jumps to next step
    time.sleep(3)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    goToBattleTab1 = driver.find_element_by_xpath('//*[@id="menu_item_battle"]/a')
    goToBattleTab1.click()
    time.sleep(1)
# loop1 ends #

print('Done Battle Loop')