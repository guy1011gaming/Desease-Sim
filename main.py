from scipy.stats import norm 
# Mit scipy lässt sich eine Gauß'sche Normalverteilung erzeugen 

import random
import time  

## Creating dictionary of people

peopleDictionary = []


class Person():
    def __init__(self, startingImmunity):
        if random.randint(0,100)<startingImmunity:
            self.immunity = True
        else: 
            self.immunity = False

        self.contagiousness = 0 
        self.mask = False
        self.contagiousDays = 0

        self.friends = int((norm.rvs(size = 1, loc = 0.5, scale = 0.15)[0]*10).round(0)*10)

    def wearMask(self):
        self.contagiousness /= 2

## Function to start the simulation...
def initiateSim():

    ## User inputs basic parameters for the simulation

    numPeople = int(input("Population: "))
    startingImmunity = int(input("Starting-immunity-percentage: "))
    startingInfecters = int(input("Amount of people who are infected initially: "))

    
    for x in range(0, numPeople):
        peopleDictionary.append(Person(startingImmunity))

    ## Infecting random people from the dictionary with a random contagiousness 

    for x in range(0, startingInfecters):
        peopleDictionary[random.randint(0, len(peopleDictionary) - 1)].contagiousness = int((norm.rvs(size=1, loc=0.5, scale = 0.15)[0]*10).round(0)*10)
    
    ## Adding a few parameters, adjustable for the user...

    daysContagious = int(input("For how many days shall a person stay contagiosness? "))
    lockdownDay = int(input("Day for lockdown to be enforced: "))
    maskDay = int(input("Day for masks to be used: "))
    return daysContagious, lockdownDay, maskDay


## Function for one day to be simulated

def runDay(daysContagious, lockdown):

    ## Going though every person in the dictionary

    for person in [person for person in peopleDictionary if person.contagiousness>0 and person.friends>0]:
        possibleContacts = int(person.friends/2)
        if possibleContacts>0:
            contactsToday = random.randint(0,possibleContacts)
        else:
            contactsToday = 0
        
        if lockdown == True:
            contactsToday = 0

        for i in range(0, contactsToday):
            friendInQuestion = peopleDictionary[random.randint(0, len(peopleDictionary)-1)]
            if random.randint(0,100)<person.contagiousness and friendInQuestion.contagiousness == 0 and friendInQuestion.immunity == False:
                friendInQuestion.contagiousness = int((norm.rvs(size=1, loc=0.5, scale=0.15)[0]*10).round(0)*10)
                print(str(peopleDictionary.index(person)) + " >>> " + str(peopleDictionary.index(friendInQuestion)))

        for person in [person for person in peopleDictionary if person.contagiousness>0]:
            person.contagiousDays += 1 ## Adding a day of infection to person...

            ## Finding all the people, who have gone through a whole infection...

            if person.contagiousDays > daysContagious:
                person.immunity = True 
                person.contagiousness = 0
                print("Person " + str(peopleDictionary.index(person)) + " is now immune.")

lockdown = False
daysContagious, lockdownDay, maskDay = initiateSim()
open('pandemicsave.txt', 'w').close()
saveFile = open("pandemicsave.txt", "a")

for x in range(1,100):
    if x==lockdownDay:
        lockdown == True

    if x == maskDay:
        for person in peopleDictionary:
            person.wearMask()
    
    print("DAY", x)
    runDay(daysContagious, lockdown)
    write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
    saveFile.write(write)
    print(str(len([person for person in peopleDictionary if person.contagiousness > 0])) + " people infected on this day.")

saveFile.close()