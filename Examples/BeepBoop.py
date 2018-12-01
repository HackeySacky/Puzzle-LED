## Buzzer-Fun with Morse Code function ##

import RPi.GPIO as GPIO
from time import sleep

## Pin number for the buzzer ##
buzz = 27

## Functions to run buzzer ##

def blip(n,t):
    '''
    Function takes in a pin# and time to output a beep for a duration of t
    '''
    GPIO.output(n,1)
    sleep(t)
    GPIO.output(n,0)

def trip(p,n,t):
    '''
    Function beeps pin for n amount of times for a duration of t
    Input: (pin,n,t)
    '''
    for x in range(n):
        blip(n,t)
        sleep(t)

def W_morse(pin,word,t = .05):
    '''
    Input: (pin,string,time) string must only contain a-z (lowercase) and spaces
    Output: Beeps the string in morse code with a time of t between beeps
    '''
    # Dictionary
    morse = {'a': [1,0,1,1,1,0],'b': [1,1,1,0,1,0,1,0,1,0],'c': [1,1,1,0,1,0,1,1,1,0,1,0],
             'd': [1,1,1,0,1,0,1,0],'e': [1,0],'f': [1,0,1,0,1,1,1,0,1,0],
             'g': [1,1,1,0,1,1,1,0,1,0],'h': [1,0,1,0,1,0,1,0],'i': [1,0,1,0],
             'j': [1,0,1,1,1,0,1,1,1,0,1,1,1,0],'k': [1,1,1,0,1,0,1,1,1,0],
             'l': [1,0,1,1,1,0,1,0,1,0],'m': [1,1,1,0,1,1,1,0],
             'n': [1,1,1,0,1,0],'o': [1,1,1,0,1,1,1,0,1,1,1,0],'p': [1,0,1,1,1,0,1,1,1,0,1,0],
             'q': [1,1,1,0,1,1,1,0,1,0,1,1,1,0],'r': [1,0,1,1,1,0,1,0],'s': [1,0,1,0,1,0],
             't': [1,1,1,0],'u': [1,0,1,0,1,1,1,0],
             'v': [1,0,1,0,1,0,1,1,1,0],'w': [1,0,1,1,1,0,1,1,1,0],'x': [1,1,1,0,1,0,1,0,1,1,1,0],
             'y': [1,1,1,0,1,0,1,1,1,0,1,1,1,0],'z': [1,1,1,0,1,1,1,0,1,0,1,0],' ': [0,0,0,0]}

    # Empty list for converting
    dit = []
    # for loop converting one letter at a time to morse code
    for x in word.lower():  # converts each letter in the string to lowercase
        dit = dit+morse[x]+[0,0] # the [0,0] are used for separtion between characters

    dit = dit + morse[' '] # adds separation between words incase this function is looped or ran in succession

    Morse(pin,dit,t) # The helper function that takes the converted string and outputs as beeps


def Morse(pin,binary,t = .05):
    '''
    Takes a list of binary (1 or 0) and converts 1 to beep on and 0 to beep off with a delay of t
    '''
    for x in binary:
        if x == 1:
            GPIO.output(pin,1)
            sleep(t)
        if x == 0:
            GPIO.output(pin,0)
            sleep(t)

if __name__ == '__main__': ## Demo (beeps sos)
    try:

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buzz,GPIO.OUT, initial = 0)

        while True:
            W_morse(buzz,'sos',.05)

    except KeyboardInterrupt:
        GPIO.cleanup()
