from SendMusicToYoutube import main as SendToYoutube
from GetMusicFromSpotify import main as Spotify
from GetMusicFromYoutube import main as GetFromYoutube



def main():

    # get my music from spotify
    Spotify()

    # get my music from Youtube
    GetFromYoutube()

    # send music to Youtube
    SendToYoutube()

main()