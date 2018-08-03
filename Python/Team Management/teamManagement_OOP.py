#! /usr/bin/python

class Player :
    name = ''
    phoneNumber = 0
    jerseyNumber = 0
    #initializer method
    def __init__(self, name, phoneNumber, jerseyNumber):
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__jerseyNumber = jerseyNumber

    #Mutator Methods
    def setName(self, name):
        self.__name = name

    def setPhone(self, number):
        self.__phoneNumber = number

    def setJersey(self, number):
        self.__jerseyNumber = number

    #Accessor Methods
    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phoneNumber

    def getJersey(self):
        return self.__jerseyNumber

    def printPlayer(self):
        print('Name: ', self.getName())
        print('Phone Number: ', self.getPhone())
        print('Jersey Number: ', self.getJersey())
        return

 #End of Class

#Program functions
def printMenu(): #This function prints the Main Menu
    print('==========Main Menu============')
    print('1. Display Team Roster.')
    print('2. Add Player.')
    print('3. Remove Player.')
    print('4. Edit Player.')
    print('9. Exit Program.\n')
    return int(input('Menu Option: '))

def addPlayer(thisTeam): #This function adds a new player to the roster
    newName = input('Enter the new player\'s Name: ')
    newPhone = input('Enter the new player\'s Phone Number: ')
    newJersey = input('Enter the new player\'s Jersey Number: ')
    newPosition = input('Enter the new player\'s Position: ')
    thisTeam[newPosition] = Player(newName, newPhone, newJersey)
    print(newName, 'has been added to the roster at', newPosition,'\n')
    return thisTeam

def editPlayer(thisTeam):
    oldPosition = input('Enter the POSITION you wish to edit: ')
    if oldPosition in thisTeam:
        updatedName = input('Enter the player\'s correct name: ')
        updatedPhone = input('Enter the player\'s correct phone number: ')
        updatedJersey = input('Enter the player\'s correct jersey number: ')
        thisTeam[oldPosition] = Player(updatedName, updatedPhone, updatedJersey)
        print(updatedName,'\b\'s info has been updated.\n')
    else:
        print('Position not found. Please try again.\n')
    return thisTeam

def removePlayer(thisTeam):
    removePosition = input('Which POSITION do you want to delete player info: ')
    if removePosition in thisTeam:
        del thisTeam[removePosition]
        print('The information for ', removePosition,' has been deleted.')
    else:
        print('Position not found. Please try again.')
    return thisTeam

def printTeam(thisTeam):
    if len(thisTeam) == 0:
        print('There are no players on this team!')
    else:
        print('Team Roster')
        print('----------------')
        for x in thisTeam.keys():
            print('\nPosition: ', x)
            thisTeam[x].printPlayer()
            print('\n')
    return

#End of Program Functions

#Main Program Code
#Initialization of Objects, Variables, etc.
myTeam = {} #Team Roster Data Dictionary

#Program Execution
print('Welcome to Tony\'s Team Manager Program 2.0')
mySelection = printMenu() #Used for menu control
while mySelection != 9:
    if mySelection == 1:
        printTeam(myTeam)
    elif mySelection == 2:
        myTeam = addPlayer(myTeam)
    elif mySelection == 3:
        myTeam = removePlayer(myTeam)
    elif mySelection == 4:
        myTeam = editPlayer(myTeam)
    mySelection = printMenu()
print('Thank you for choosing Tony\'s Team Manager Program 2.0! Have a nice Day!!')
#End of Main Program
