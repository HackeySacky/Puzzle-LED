## Light w/ Encoder Input ##

from Lights import *
from Rotary import *
from Colors import *
from time import sleep

#-------LED-CONFIG------------------------------------------#
COUNT       = 12
PIN         = 18
FREQUENCY   = 800000
DMA         = 10
BRIGHTNESS  = 20
INVERT      = False
CHANNEL     = 0
Board_Type  = ws.SK6812_STRIP_RGBW
#-------Convert-To-Object-----------------------------------#
ring = Adafruit_NeoPixel(
        COUNT,PIN,FREQUENCY,DMA,INVERT,BRIGHTNESS,CHANNEL,Board_Type)
ring.begin() # setup for the IO
#--------Rotary-Encoder-------------------------------------#
CLK_PIN = 2 
DT_PIN =  3
SW_PIN =  4
#-----------Rotory-Encoder-OBJ------------------------------#
k = Knob(CLK_PIN,DT_PIN,SW_PIN)
start(k) # setup for IO and interupts
#-----------------------------------------------------------#

pled = Colors(ring.numPixels(),'Red')

try:
    print('Ready')
    colorlist(ring,pled.now)
    n = range(ring.numPixels())
    current = 0
    
    while not pled.iswin():
        
        Knob.rot = 0
        Knob.click = 0

        c_blink(ring,n[current],1,.1)
        
        if Knob.click == 1:
            print('click')
            if pled.now.count(Colors.c['Red']) >= (pled.n-2):
                pled.Sneaky(current)
            else:
                pled.colorChange(current)
            colorlist(ring,pled.now)
            
        if Knob.rot != 0:
            current -= Knob.rot
            if current == len(n) or current == -len(n):
                current = 0
            print(current)
    print('We have a Winner!')
    sleep(1)
    lightshow(ring,[280,0,280,0],[232, 239, 38,0],3)
    ledclear(ring)

except KeyboardInterrupt:
    ledclear(ring)

