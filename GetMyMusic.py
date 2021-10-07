from os import error
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import loginDetails
# imports to wait for page to load
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# =============== function that logs in from the Hamburger menu on Spotify ===============


def hamburgerLogin(browser):
    browser.get("https://www.spotify.com")

    # click hamburger
    WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/div[1]/header/div/div[2]/button'))
    ).click()

    # click login
    time.sleep(2)
    WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mh-mobile-navigation"]/ul/li[6]/a'))
    ).click()


# =============== login function after logging in from spotify Hamburger menu ===============
def enterUsername_Password(browser):
    username = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='username']"))
    )
    time.sleep(random.randint(1, 2))
    username.send_keys(loginDetails.username)

    password = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='password']"))
    )
    time.sleep(random.randint(1, 2))
    password.send_keys(loginDetails.password)


# =============== login function after logging in from spotify Hamburger menu ===============
def login(browser):

    hamburgerLogin(browser)

    enterUsername_Password(browser)

    # click login button
    time.sleep(1)
    WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()
    time.sleep(5)

    # press (x) on irrelevent pop-ups
    try:
        pop_up = WebDriverWait(browser, 25).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[15]/div/div/div/div[2]/button[2]'))
        )
        time.sleep(20)
        pop_up.click()
    except Exception as e:
        print("\nError: ", e)

    try:
        cookieBanner = WebDriverWait(browser, 25).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="onetrust-close-btn-container"]/button'))
        )
        time.sleep(2)
        cookieBanner.click()
    except Exception as e:
        print("\nError: ", e)

    time.sleep(5)


# =============== Function that removes duplicates from a list ===============
def removeDuplicates(listOfSongs):
  return list(dict.fromkeys(listOfSongs))


# =============== Function that writes the song names to a file ===============
def writeToFile(listOfSongs):
    with open("myLikedSongs.txt", "w") as w_file:
        for song in listOfSongs:
            w_file.write(song + "\n")


# =============== Main Method ===============
def getTracks(browser):
    # go to liked songs playlist
    browser.get("https://open.spotify.com/collection/tracks")
    browser.maximize_window()
    time.sleep(2)

    listOfSongNames = []
    try:
        print("\nGetting song name\n")
        songInDOM = WebDriverWait(browser, 15).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '[class="_gvEBguxvbSruOQCkWrz standalone-ellipsis-one-line ipxcyIaAWQfeUHO468Os"]'))
            )

        while songInDOM:
            try:
                # gets a list of song elements
                listOfSongs = WebDriverWait(browser, 15).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, '[class="jqC4kulx5rkKJSJHwWC0"]'))
                )
                #  add the text of the elements into a list
                for song in listOfSongs:
                    text = song.text.replace('\nE\n', ' ')
                    listOfSongNames.append(text.replace('\n', ' '))
                    print(text)

                lastSong = listOfSongs[-1]
            except Exception as e:
                print(f"\nError: {e}\n")

            # scroll the song into view
            try:
                browser.execute_script("arguments[0].scrollIntoView()", lastSong)
            except Exception as e:
                print("\nError: ", e)

            # if the last song is "hate u love u" than break
            if lastSong.text == "hate u love u\nOlivia O'Brien":
                print("\nGot all Songs from Liked playlist!")

                # remove any duplicate songs from the list
                listOfSongNames_noDups = removeDuplicates(listOfSongNames)
                print(f"Number of songs: {len(listOfSongNames_noDups)}")
                
                # write the songs to a file
                try:
                    writeToFile(listOfSongNames_noDups)
                    print("\nSongs written to text file.\n")
                    break
                except Exception as e:
                    print(f"\nError: {e}")

    except Exception as e:
        print("Error: ", e)

    print("\ngonna sleep now!")

    # get the name of the song

    # get the first artist


# =============== Main Method ===============
def main():
    browser = webdriver.Chrome(
        executable_path='C:/Users/Ismail/Documents/Automated Bot/SeleniumAndDriver/chromedriver_win32/chromedriver')

    login(browser)

    getTracks(browser)

    time.sleep(30)


main()
