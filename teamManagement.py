#!/usr/bin/env python3

# Methods

# This method prints the menu and accepts input from user.
def printMenu():
    print('==========Main Menu============')
    print('1. Display Team Roster.')
    print('2. Add Member.')
    print('3. Remove Member.')
    print('4. Edit Member')
    print('9. Exit Program')
    selection = str(input('Menu Option: '))
    return selection

#This method adds a new teammember to the list
def addPerson(teamList):
    newPerson = input('Enter the new teammember\'s name: ')
    teamList.append(newPerson)
    print('Here\'s the updated team list:')
    printTeam(teamList)
    return teamList

#this method removes a teammeber from the list
def removePerson(teamList):
    printTeam(teamList)
    name = int(input('Who do you want to remove from the team: '))
    teamList.pop(name)
    print('Here\'s the updated team list:')
    printTeam(teamList)
    return teamList

#this method allows the user to edit a teammember
def editPerson(teamList):
    printTeam(teamList)
    playerNumber = int(input('Which player do you want to edit: '))
    teamList.pop(playerNumber)
    newPlayer = input('Enter the replacement info: ')
    teamList.insert(playerNumber, newPlayer)
    print('Here\'s the updated team list:')
    printTeam(teamList)
    return teamList

#this method prints the current team roster
def printTeam(teamList):
    for c in range(len(teamList)):
        print('Player[', c, '] =', teamList[c])
    return

#This is the main method
print('Welcome to Tony\'s Team Manager Program')
myTeam = ['Bob', 'Harry', 'Sam'] #I used three random names to start the list. The project description stated that there were some regulars. These names represent those people.
mySelection = str(printMenu())
while mySelection != '9' :
    if mySelection == '1':
        printTeam(myTeam)
        mySelection = printMenu()
    elif mySelection == '2':
        addPerson(myTeam)
        mySelection = printMenu()
    elif mySelection == '3':
        removePerson(myTeam)
        mySelection = printMenu()
    elif mySelection == '4':
        editPerson(myTeam)
        mySelection = printMenu()
    elif mySelection == '9':
        print('Goodbye!')
    else :
        print('Option not found. Please try again.')
        mySelection = printMenu()


