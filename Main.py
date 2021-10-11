from selenium import webdriver
from SendMusicToYoutube import main as Youtube
from GetMusicFromSpotify import main as Spotify



def main():
    browser = webdriver.Chrome(
            executable_path='C:/Users/Ismail/Documents/Automated Bot/SeleniumAndDriver/chromedriver_win32/chromedriver')

    browser.set_window_size(width=1300, height=1045)
    browser.set_window_position(0, 0)

    # get my music from spotify
    Spotify(browser)

    # send music to Youtube
    Youtube(browser)

