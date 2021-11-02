from os import stat
from re import search

# =============== function that writes an song to a file ===============
def writeSongToFile(song, file_path):
    with open(file_path, 'a+') as w_file:
        w_file.seek(0)  # set pointer to beginning of file
        file = w_file.read().splitlines()  # remove newline
        if song in file:
            print(f"{song} exists in file")
        else:
            w_file.write(song + "\n")
            print(f"{song} added to file")


# =============== Function that writes a list of songs to a file ===============
def writeListOfSongsToFile(listOfSongs, file_path):
    try:
        with open(file_path, "w") as w_file:
            for song in listOfSongs:
                w_file.write(song + "\n")
        print("\nSongs written to text file.\n")

    except Exception as e:
        print(f"\nError writting to file: {e}")


# =============== function that removes an song from a file ===============
def removeSongFromFile(song, file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    with open(file_path, "w") as f:
        for line in lines:
            if line.strip("\n") != song:
                f.write(line)
    
    print(f"{song} removed from file")


# =============== function that checks if an song exists in a file ===============
def checkIfSongExistsInFile(song, file_path):
    with open(file_path, 'a+') as w_file:
        w_file.seek(0)  # set pointer to beginning of file
        file = w_file.read().splitlines()  # remove newline
        if song in file:
            return True
        else:
            return False


# =============== function that finds subStrings in each line of a file ===============
def removeIrrelevantSongs(subString, file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    with open(file_path, "w") as f:
        for line in lines:
            if search(subString, line):
                print("=====" , line.strip("\n"), " removed from file!")
                
            else:
                # print(f"{subString} not in this line.")
                f.write(line)
                

# =============== function that checks the size of a file ===============
def getSizeOfFile(file_path):
    return stat(file_path).st_size



songsRetrieved_FilePath = "C:\\Users\\Ismail\\Documents\\Spotify_Scraper\\textFiles\\songsRetrieved.txt"
songsSent_FilePath = "C:\\Users\\Ismail\\Documents\\Spotify_Scraper\\textFiles\\songsSent.txt"