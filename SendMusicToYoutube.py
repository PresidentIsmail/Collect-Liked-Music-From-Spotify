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
def signIn(browser):

    enterEmailAndPassword(browser, email, email_password)

    time.sleep(3)

    # If "Protect Your Account Page" opens
    try:
        protectYourAccount(browser)
    except:
        pass


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
        search.send_keys(Keys.ENTER)

    except Exception as e:
        print(f"Search Error: {e}")


# ============ Function that right clicks on the song using ActionChains
def rightClickOnSong(browser):
    # use ActionChains to right-click on the song
    actions = ActionChains(browser)
    try:
        topResultSong = WebDriverWait(browser, 15).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '[id="content"]')) 
                )
        actions.move_to_element(topResultSong).perform()
        time.sleep(1)
        actions.context_click(topResultSong).perform()
        time.sleep(2)
    except Exception as e:
        print(f"Top Result Error: {e}")


# ============ Function that likes songs and adds them to Liked songs
def addSongToLikes(browser, songsLiked):
    try:
        like = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="items"]/ytmusic-toggle-menu-service-item-renderer[2]'))
                )

        if like.text == "Add to liked songs":
            like.click()
            print(f"Songs liked: {songsLiked}")
            songsLiked += 1
        else:
            pass

    except Exception as e:
        print(f"Like Error: {e}")



# ============ Function searches for the each song in the text file and likes it on youtube Music
def searchForSong(browser, file_path):
    with open(file_path, "r") as file:
        
        songsLiked = 0

        for song in file:
            song = song.replace("\n", "")

            # search for the song
            searchforSongOnYoutube(browser, song)

            # right click the song to bring up the menu
            rightClickOnSong(browser)

            # like the song
            addSongToLikes(browser, songsLiked)
            
            # exit to home page
            time.sleep(2)
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="left-content"]/a/picture[1]/img'))
            ).click()

            time.sleep(random.randint(2, 4))



# ============ Main Method
def main():
    browser = webdriver.Chrome(
        executable_path='C:/Users/Ismail/Documents/Automated Bot/SeleniumAndDriver/chromedriver_win32/chromedriver')
    file_path = "mylikedSongs.txt"
    time.sleep(3)

    browser.set_window_size(width=1080, height=1045)
    browser.set_window_position(0, 0)
    signIn(browser)

    # browser.maximize_window()
    searchForSong(browser, file_path)

    time.sleep(5)


main()
