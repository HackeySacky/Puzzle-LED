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

    for x in range(0,num):
        ledobj.setPixelColor(n,color)
        ledobj.show()
        time.sleep(t)
        ledobj.setPixelColor(n,Color(0,0,0))
        ledobj.show()
        time.sleep(t)
        
def c_blink(ledobj,n,num = 1, t = 1):
    
    for x in range(0,num):

        color = ledobj.getPixelColor(n)
        
        ledobj.setPixelColor(n,Color(255,255,255,255))
        ledobj.show()
        time.sleep(t)
        ledobj.setPixelColor(n,color)
        ledobj.show()
        time.sleep(t)

def colorize(ledobj,color):
    for n in range(ledobj.numPixels()):
        ledobj.setPixelColor(n,color)
    ledobj.show()

def Color_L(l):
    G, R, B, W = l
    return Color(R,G,B,W)

def colorlist(ledobj,cList):
    for n in range(len(cList)-1):
        ledobj.setPixelColor(n,Color_L(cList[n]))
    ledobj.show()
