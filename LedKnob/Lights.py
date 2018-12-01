import time
from neopixel import *


def ledclear(strip, wait_ms = 50):
    '''
    Clears the Colors on display
    '''
    for c in range(strip.numPixels()):
        strip.setPixelColor(c,Color(0,0,0))
        strip.show()
        time.sleep(wait_ms/1000.0)

def blink(ledobj,n,color,num = 1,t = 1):
    ''' Blinks white num times over time t
        in the color([r,g,b,w]) at postion n
    '''

    for x in range(0,num):
        ledobj.setPixelColor(n,color)
        ledobj.show()
        time.sleep(t)
        ledobj.setPixelColor(n,Color(0,0,0))
        ledobj.show()
        time.sleep(t)
        
def c_blink(ledobj,n,num = 1, t = 1):
    ''' flashes white num times over time t
        at postion n
    '''
    
    for x in range(0,num):

        color = ledobj.getPixelColor(n)
        
        ledobj.setPixelColor(n,Color(255,255,255,255))
        ledobj.show()
        time.sleep(t)
        ledobj.setPixelColor(n,color)
        ledobj.show()
        time.sleep(t)

def colorize(ledobj,color):
    ''' sets all the leds to a color
    '''
    for n in range(ledobj.numPixels()):
        ledobj.setPixelColor(n,color)
    ledobj.show()

def lightshow(ledobj,c1,c2,n,t = .5):
    ''' Flashes between two colors [r,g,b,w] n times over time t
    '''
    
    color =  Color_L(c1)
    color2 = Color_L(c2)
    
    for x in range(n):
        colorize(ledobj,color)
        time.sleep(t)
        colorize(ledobj,color2)
        time.sleep(t)
    colorize(ledobj,Color(0,0,0))

def Color_L(l):
    ''' Helper function that separates a list
        and returns the color [R,G,B,W]
    '''
    G, R, B, W = l
    return Color(R,G,B,W)

def colorlist(ledobj,cList):
    '''Takes a list containting a list of colors and changes the
       colors of all the leds 
    '''
    for n in range(len(cList)):
        ledobj.setPixelColor(n,Color_L(cList[n]))
    ledobj.show()
