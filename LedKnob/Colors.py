## Color Dictionary and Display data storage
import random
from time import sleep

class Colors:
    '''
    Dictionary of Colors that will be used in the game
    '''
    c = { 'Red': [255,0,0,0],
          'Green': [0,255,0,0],
          'Blue': [0,0,255,0],
          }
    
    def __init__(self,n,win):
        '''
        Creates a list of len(n) containing a color from the dictionary
           Ex. Colors(12,'Red')
        '''
        self.n =n
        self.now = []
        self.win = list([Colors.c[win] for x in range(n)])
        self.Scramble()

    def fix(self, index):
        '''
        Returns an index value in a loop, if the index is larger than the length
        then the remainder is returned in both the positive and negative direction
        '''
        if index > self.n - 1:
            return index % self.n
        elif index < -(self.n - 1):
            return index % self.n
        return index

    def colorChange(self,pos):
        '''
        Changes the color of a position self.now based on the selected position's color
        '''

        self.previous = self.now
        
        if self.now[pos] == Colors.c['Red']:
            k = pos - 1
            k = self.fix(k)
            self.now[k] = Colors.c['Green']
        elif self.now[pos] == Colors.c['Blue']:
            k = pos + 2
            k = self.fix(k)
            self.now[k] = Colors.c['Red']
        elif self.now[pos] == Colors.c['Green']:
            k = pos - 2
            k = self.fix(k)
            self.now[k] = Colors.c['Blue']

    def Sneaky(self,pos):
        '''
        Changes Blue to Red and the other colors the same as colorChange
        '''
        if self.now[pos] == Colors.c['Blue']:
            self.now[pos] = Colors.c['Red']
        else:
            self.colorChange(pos)

    def Scramble(self):
        self.now = [Colors.c[random.choice(['Red','Green','Blue'])] for x in range(self.n)]

    def iswin(self):
        return self.now == self.win
