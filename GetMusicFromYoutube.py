from os import error
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from loginDetails import email, email_password

# imports to wait for page to load
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# imports for file handling
from FileHandling import writeListOfSongsToFile
from FileHandling import songsRetrieved_FilePath

# imports for logging into youtube music
from SendMusicToYoutube import signIn


# =============== Function that removes duplicates from a list ===============
def removeDuplicates(listOfSongs):
    return list(dict.fromkeys(listOfSongs))


# =============== function that scrolls through the playlist ===============
def scrollPlaylist(browser, lastSong):
    try:
        browser.execute_script(
                    "arguments[0].scrollIntoView()", lastSong)
    except Exception as e:
        print("\nError: ", e)


# =============== function that gets the songs into a list ===============
def putSongsIntoList(browser):
    listOfSongs = WebDriverWait(browser, 15).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, '[class="jqC4kulx5rkKJSJHwWC0"]'))
                )
    
    return listOfSongs


# ============ Function that gets my music from Youtube Music
def collectMusic(browser):
    # go to playlist of liked songs
    browser.get("https://music.youtube.com/playlist?list=LM")
    time.sleep(3)

    listOfSongNames = []
    try:

        while True:
            try:
                # gets a list of song elements
                listOfSongs = putSongsIntoList(browser)

                #  add the text of the elements into another list
                for song in listOfSongs:
                    text = song.text.replace('\nE\n', ' ')
                    listOfSongNames.append(text.replace('\n', ' '))
                    print(text)

                lastSong = listOfSongs[-1]
            except Exception as e:
                print(f"\nError: {e}\n")

            # scroll the song into view
            scrollPlaylist(browser, lastSong)

            # if the last song is "hate u love u" than break
            if lastSong.text == "hate u love u\nOlivia O'Brien":
                print("\nGot all Songs from Liked playlist!")

                # remove any duplicate songs from the list
                listOfSongNames_noDups = removeDuplicates(listOfSongNames)
                print(f"Number of songs: {len(listOfSongNames_noDups)}")

                # write the songs to a file
                writeListOfSongsToFile(listOfSongNames_noDups, songsRetrieved_FilePath)
                break

    except Exception as e:
        print("Error Collecting Songs: ", e)

    

# ============ Main Method
def main():
    browser = webdriver.Chrome(
        executable_path='C:/Users/Ismail/Documents/Automated Bot/SeleniumAndDriver/chromedriver_win32/chromedriver')
    time.sleep(3)

    browser.set_window_size(width=1300, height=1045)
    browser.set_window_position(0, 0)

    # Sign into Youtube Music
    signIn(browser)

    # CollectMusic
    collectMusic(browser)