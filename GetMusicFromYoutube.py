import time
from selenium import webdriver

# imports to wait for page to load
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# imports for file handling
from FileHandling import writeListOfSongsToFile
from FileHandling import songsRetrieved_FilePath

# imports for logging into youtube music
from LoginToYoutubeBrowser import signIn
from loginDetails import youtube_musicGetting_email, youtube_musicGetting_password



# =============== Function that removes duplicates from a list ===============
def removeDuplicates(listOfSongs):
    return list(dict.fromkeys(listOfSongs))


# =============== function that scrolls through the playlist ===============
def scrollPlaylist(browser, lastSong):
    try:
        browser.execute_script(
                    "arguments[0].scrollIntoView()", lastSong)
        time.sleep(2)
    except Exception as e:
        print("\nScroll Error: ", e)


# =============== function that gets the songs into a list ===============
def putSongsIntoList(browser):
    listOfSongs = WebDriverWait(browser, 15).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, '[class="flex-columns style-scope ytmusic-responsive-list-item-renderer"]'))
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
                    textList = song.text.rsplit("\n", 1)
                    text = textList[0].replace("\n", " ").replace("&", "and")
                    listOfSongNames.append(text)
                    print(text)

                lastSong = listOfSongs[-1]
            except Exception as e:
                print(f"\nError: {e}\n")

            # scroll the song into view
            scrollPlaylist(browser, lastSong)

            # if the last song is "hate u love u" than break
            if any("Magnolia" in line.text for line in listOfSongs):
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
    signIn(browser, youtube_musicGetting_email, youtube_musicGetting_password)

    # CollectMusic
    collectMusic(browser)