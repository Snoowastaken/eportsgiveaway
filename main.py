# This program randomly chooses winners from a list of people why also having the ability to remove people from the
# list, so they aren't chosen in the winners list. This program also will prevent duplicate winners from winning.

# Imports the random module
import random


# Gets how many people are trying to win in the giveaway
def getsize():
    input_size = input("How many people are in the running? ")
    return input_size


# Creates a list of people who are in the running based on the size gotten from getsize() and appends the list with
# numbers starting from 1 to the size of the list. Also prints the mainList
# example: mainList = [1,2,3,4,5] if size = 5
def createmainList(size):
    mainList = []
    for i in range(int(size)):
        mainList.append(i + 1)
    print("The mainList contains: ", mainList)
    return mainList


# Removes those who are not in the running from the mainList so they are not chosen in the winners list.
# Example: mainList = [1,2,3,4,5] if size = 5 and if you want to remove the numbers 3 and 4 from the mainList then the
# mainList would be [1,2,5]. This is so officers are not chosen in the winners list mostly.
def removefrommainList(mainList):
    howmany = input("How many people are being removed from the mainList? ")
    i = 0
    while i < int(howmany):
        removed = input("Who is being removed? ")
        if int(removed) not in mainList:
            print("That person is not in the mainList.")
        else:
            mainList.remove(int(removed))
            i += 1
    print("The mainList now contains: ", mainList)
    return mainList


# Chooses the winners from the mainList and creates a new list of the winners and then prints the winners list.
# Example: mainList = [1,2,3,4,5] and you want to pick 3 winners from the mainList then the winners list would be
# randomly chosen from the mainList and then added to the winners list and removed from the mainList to prevent
# duplicates. The winners list could be [5, 3, 2] possibly.
def choosewinner(mainList):
    howmanywin = input("How many people are being chosen to win? ")
    i = 0
    winList = []
    while i < int(howmanywin):
        winner = random.choice(mainList)
        winList.append(winner)
        mainList.remove(winner)
        i += 1
    print("The winners are:", winList)
    return winList


# calls all the functions and does the actual program.
choosewinner(removefrommainList(createmainList(getsize())))
