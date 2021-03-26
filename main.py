from scipy.stats import norm 
# Mit scipy lässt sich eine Gauß'sche Normalverteilung erzeugen 

import random
import time  

class Person():
    def __init__(self, startingImmunity):
        if random.randint(0,100)<startingImmunity:
            self.immunity = True
        else: 
            self.immunity = False

        self.contagiousness = 0 
        self.mask = False
        self.schädlicheTage = 0

        self.friends = int((norm.rvs(size = 1, loc = 0.5, scale = 0.15)[0]*10).round(0)*10)

        def wearMask():
            self.contagiousness /= 2


def initiateSim:
    numPeople = int(input("Population: "))
      
