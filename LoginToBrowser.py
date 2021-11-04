from os import error
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# imports to wait for page to load
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# ============ Function gets past "Protect Your Account" page
def protectYourAccount(browser):
    # click confirm
    confirm = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div'))
    )
    confirm.click()


# ============ Function enters signin email and password
def enterEmailAndPassword(browser, email, email_password):
    # go to sing in page
    browser.get("https://accounts.google.com/signin/v2/identifier?ltmpl=music&service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fmusic.youtube.com%252F%26feature%3D__FEATURE__&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    # enter email
    emailBox = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="email"]'))
    )
    emailBox.send_keys(email)
    time.sleep(2)
    # click next
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[jsname="V67aGc"]'))
    ).click()

    # enter password
    passwordBox = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="password"]'))
    )
    passwordBox.send_keys(email_password)
    time.sleep(2)
    # click next
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="passwordNext"]/div/button/span'))
    ).click()


# ============ Function that signs into YouTube
def signIn(browser, email, email_password):

    enterEmailAndPassword(browser, email, email_password)

    time.sleep(3)

    # If "Protect Your Account Page" opens
    try:
        protectYourAccount(browser)
    except:
        pass
