#!/usr/bin/python
#-*-coding: utf-8 -*-
#This program obtains date on height and weight from the user and then calculates the BMI based on that data.


#Methods

#This method obtains the name of the person from the user.
# NOTE: This method should be run before the getWeight and getHeight methods
def getName():
    thisName = str(input('What is the Person\'s name or \'q\' to quit:  '))
    if thisName == 'q':
        print('Goodbye!')
    return thisName

def getWeight(): #This method obtains the weight from the user
    thisWeight = float(input('What is their weight  in pounds:  '))
    return thisWeight

def getHeight(): #This method obtains the height from the user
    thisHeight = float(input("What is the their height in inches:  "))
    return thisHeight

def calcBMI(weight, height): #This method calculates the BMI
    thisBMI = (weight*703)/(height*height)
    return thisBMI

def displayBMI(name, weight, height, BMI):
    print(name, '\'s BMI Profile:',)
    print('------------------')
    print('Height:  ', height, ' inches')
    print('Weight:  ', weight, ' pounds')
    print('BMI Index:  ', format(BMI, '.2f'))
    return

#Main Method
userName = str(getName())
while userName != 'q':
    userWeight = getWeight()
    userHeight = getHeight()
    BMI = calcBMI(userWeight, userHeight)
    displayBMI(userName, userWeight, userHeight, BMI)
    userName = str(getName())

#End of Main Method
