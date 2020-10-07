#!/usr/bin/env python3
from selenium import webdriver
import selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display  
import time
from datetime import datetime
import pytz
import sys

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox") 
options.add_argument("--disable-setuid-sandbox") 
options.add_argument("--disable-dev-shm-using") 
options.add_argument("--disable-extensions") 
options.add_argument("--disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument('allow-file-access-from-files')
options.add_argument('use-fake-ui-for-media-stream')

driver = webdriver.Chrome(options=options)
# tz_INDIA = pytz.timezone('Asia/Kolkata')
# currTime = datetime.now(tz_INDIA).strftime("%H:%M")
# given_time = "9:30"
# while currTime != given_time:
#     currTime = datetime.now(tz_INDIA).strftime("%H:%M")
#     time.sleep
# if currTime == given_time:
Subject = sys.argv[1]
Roll = sys.argv[2]
Pass = sys.argv[3]
driver.get("https://teams.microsoft.com/_?culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school/conversations/General?threadId=19:e55d2df493ee4cb296c880eba5a0675b@thread.tacv2&ctx=channel")
def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True
def join_call_fn():
    try:
        join_call = WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Join')]")))
        join_call.click()
        try:
            no_video = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"page-content-wrapper\"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button")))
            if no_video.get_attribute("title") == "Turn camera off":
                no_video.click()
            else:
                pass
            no_audio = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"preJoinAudioButton\"]")))
            if no_audio.get_attribute("title") == "Mute microphone":
                no_audio.click()
            join_now = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"page-content-wrapper\"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button")))
            join_now.click()
            try:
                aria_label = WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-label=\"Show participants\"]")))
                aria_label.click()
                organiser = driver.find_element_by_xpath("//*[contains(text(),'Organiser')]")
                while organiser is not None:
                    driver.implicitly_wait(300)
                    organiser = driver.find_element_by_xpath("//*[contains(text(),'Organiser')]")
                    continue
            except NoSuchElementException:
                driver.find_element_by_xpath("//*[@aria-label=\"Hang up\"]").click()
                print('Organiser not present')
                driver.close()
                sys.exit(0)
        except WebDriverException or NoSuchElementException:
            try:
                pass
            except WebDriverException:
                pass
    except WebDriverException or NoSuchElementException:
        try:
            refresh_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"page-content-wrapper\"]/div[1]/middle-messages-stripe/div/messages-header/div[2]/div/message-pane/tab-takeover/div/div[3]/button")))
            refresh_btn.click()
            join_call_fn()
        except WebDriverException or NoSuchElementException:
            driver.execute_script("alert(\"Class hasn't started yet!\");")
            pass
try:
    login_email = WebDriverWait(driver,600).until(EC.presence_of_element_located((By.NAME,"loginfmt")))
    login_email.send_keys(Roll+"@nitt.edu")
    login_email_submit = WebDriverWait(driver,600).until(EC.element_to_be_clickable((By.ID,"idSIButton9")))
    login_email_submit.click()
    login_pass = WebDriverWait(driver,600).until(EC.presence_of_element_located((By.NAME,"passwd")))
    login_pass.send_keys(Pass)
    login_pass_submit = WebDriverWait(driver,600).until(EC.element_to_be_clickable((By.XPATH,"//*[@value=\"Sign in\"]")))
    login_pass_submit.click()
    stay_button_no = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID,"idBtn_Back")))
    stay_button_no.click()
    use_app = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Use the web app instead')]")))
    use_app.click()
except TimeoutException:
    pass
except WebDriverException:
    try:
        driver.execute_script("alert(\"Element didn't load in the stipulated time\");")
    except WebDriverException:
        pass
    time.sleep(2)
    driver.close()
try:
    card = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CLASS_NAME,"team-card")))
    if len(driver.find_elements_by_class_name("team-name-text"))>0:
        count = 0
        for subject in driver.find_elements_by_class_name("team-name-text"):
            if subject.text == Subject :
                subject.click()
                break
            count = count + 1
        if count == len(driver.find_elements_by_class_name("team-name-text")):
            driver.execute_script("alert(\"Invalid Subject\");")
            sys.exit(0)
    join_call_fn()
except WebDriverException or NoSuchElementException:
    try:
        driver.execute_script("alert(\"Specified card not present at the moment\");")
    except WebDriverException:
        driver.quit()
        sys.exit()