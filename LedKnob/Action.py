## Light w/ Encoder Input ##

from Lights import *
from Rotary import *

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
#-----------------------------------------------------------#
k = Knob(CLK_PIN,DT_PIN,SW_PIN)
start(k) # setup for IO and interupts
#-----------------------------------------------------------#

try:
    print('Ready')
    colorize(ring,Color(0,180,180))
    n = range(ring.numPixels())
    current = 0
    
    while True:
        
        Knob.rot = 0
        Knob.click = 0

        c_blink(ring,n[current],1,.3)
        
        if Knob.click == 1:
            print('click')
            if ring.getPixelColor(n[current]) == Color(0,180,180):
                ring.setPixelColor(n[current],Color(0,0,0))
            else:
                ring.setPixelColor(n[current],Color(0,180,180))
            ring.show()
            
            
        if Knob.rot != 0:
            current -= Knob.rot
            if current == len(n) or current == -len(n):
                current = 0
            print(current)

except KeyboardInterrupt:
    ledclear(ring)

