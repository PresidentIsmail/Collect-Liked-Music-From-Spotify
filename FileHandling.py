from os import stat
from re import search

# =============== function that writes an account to a file ===============
def writeAccountToFile(account, file_path):
    with open(file_path, 'a+') as w_file:
        w_file.seek(0)  # set pointer to beginning of file
        file = w_file.read().splitlines()  # remove newline
        if account in file:
            print(f"{account} exists in file")
        else:
            w_file.write(account + "\n")
            print(f"{account} added to file")


# =============== function that removes an account from a file ===============
def removeAccountFromFile(account, file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    with open(file_path, "w") as f:
        for line in lines:
            if line.strip("\n") != account:
                f.write(line)
    
    print(f"{account} removed from file")


# =============== function that checks if an account exists in a file ===============
def checkIfAccountExistsInFile(account, file_path):
    with open(file_path, 'a+') as w_file:
        w_file.seek(0)  # set pointer to beginning of file
        file = w_file.read().splitlines()  # remove newline
        if account in file:
            return True
        else:
            return False


# =============== function that finds subStrings in each line of a file ===============
def removeIrrelevantAccounts(subString, file_path):
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



allMySongs_FilePath = "C:\\Users\\Ismail\\Documents\\Spotify_Scraper\\textFiles\\allMySongs.txt"
likedSongs_FilePath = "C:\\Users\\Ismail\\Documents\\Spotify_Scraper\\textFiles\\likedSongs.txt"