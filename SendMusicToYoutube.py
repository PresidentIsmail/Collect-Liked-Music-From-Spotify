import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# imports to wait for page to load
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# imports for file handling
from FileHandling import writeSongToFile, removeSongFromFile, checkIfSongExistsInFile
from FileHandling import songsSent_FilePath, songsRetrieved_FilePath

# imports for logging into youtube music
from LoginToYoutubeBrowser import signIn
from loginDetails import youtube_musicSending_email, youtube_musicSending_password



# ============ Function that searches for song in the youtubse search bar
def searchforSongOnYoutube(browser, song):
    # Click the Search icon
    try:
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]'))
        ).click()
    except Exception as e:
        print(f"Icon Search Error: {e}")

        # search for the song
    time.sleep(2)
    try:
        search = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, 'input'))
        )
        search.send_keys(song)
        time.sleep(1)
        search.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)

        # click on "songs" button
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[title="Show song results"]'))
        ).click()

    except Exception as e:
        print(f"Search Error: {e}")


# ============ Function that right clicks on the song using ActionChains
def rightClickOnSong(browser):

    actions = ActionChains(browser)
    try:
        topResultSong = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="contents"]/ytmusic-responsive-list-item-renderer[1]'))
        )

    except Exception as e:
        print(f"Top Result Error 1: {e}")
    
    try:
        actions.move_to_element_with_offset(topResultSong, 5, 5).context_click().perform()
        time.sleep(1)
        
    except Exception as e:
        print(f"Top Result Error 2: {e}")


# ============ Function that likes the song
def likeSong(browser):
    try:
        like = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="items"]/ytmusic-toggle-menu-service-item-renderer[2]'))
        )

        return like
    except:
        pass


# ============ Function that go back to youtubes home page
def exitToHomePage(browser):
    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="left-content"]/a/picture[1]/img'))
        ).click()
    except :
        pass


# ============ Function searches for the each song in the text file and likes it on youtube Music
def addMySongsToLikePlaylist(browser):
    with open(songsRetrieved_FilePath, "r") as file:

        songsLiked = 0

        for song in file:
            song = song.replace("\n", "")

            songExistsInFile = checkIfSongExistsInFile(song, songsSent_FilePath)

            if songExistsInFile:
                print("\nsong exits in file")
                removeSongFromFile(song, songsRetrieved_FilePath)

            else:
                browser.refresh()
                
                # search for the song
                searchforSongOnYoutube(browser, song)
                time.sleep(2)

                # right click the song to bring up the menu
                rightClickOnSong(browser)

                # like the song
                try:
                    like = likeSong(browser)
                    if like.text == "Add to liked songs":
                        like.click()

                        songsLiked += 1
                        print(f"\nSongs liked: {songsLiked}")
                        removeSongFromFile(song, songsRetrieved_FilePath)
                        writeSongToFile(song, songsSent_FilePath)
                    else:
                        removeSongFromFile(song, songsRetrieved_FilePath)
                        pass


                except Exception as e:
                    print(f"Like Error: {e}")

                # exit to home page
                exitToHomePage(browser)

                time.sleep(random.randint(2, 4))



# ============ Main Method
def main():
    browser = webdriver.Chrome(
        executable_path='C:/Users/Ismail/Documents/Automated Bot/SeleniumAndDriver/chromedriver_win32/chromedriver')
    time.sleep(3)

    browser.set_window_size(width=1300, height=1045)
    browser.set_window_position(0, 0)
    signIn(browser, youtube_musicSending_email, youtube_musicSending_password)

    # browser.maximize_window()
    addMySongsToLikePlaylist(browser)
