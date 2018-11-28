import RPi.GPIO as GPIO
import threading
from time import sleep
from gpiozero import Button

cclk = 1
cdt = 1
rot = 0
lock = threading.Lock()

class Knob:
    def __init__(self,clk = 2,dt = 3,sw = 4,w = True):
        rot = 0
        click = 0
        self.dt = dt
        self.clk = clk
        self.sw = sw
        self.warn = w


def start(obj):

    GPIO.setwarnings(obj.warn)
    GPIO.setmode(GPIO.BCM)      # Sets pin number layout
    # Sets pins clk and dt
    GPIO.setup(obj.clk,GPIO.IN)
    GPIO.setup(obj.dt,GPIO.IN)
    obj.button = Button(obj.sw)

    obj.button.when_pressed = clack
    obj.button.when_released = click
    GPIO.add_event_detect(obj.clk,GPIO.RISING,callback=boop)
    GPIO.add_event_detect(obj.dt,GPIO.RISING,callback=boop)
    return

def click():
    Knob.click = 1
    
def clack():
    Knob.click = 0


def boop(x):
    global cclk,cdt,rot,lock

    clk = GPIO.input(2)
    dt = GPIO.input(3)

    if cclk == clk and cdt == dt:
        return

    cclk = clk
    cdt = dt

    if (clk and dt):
        lock.acquire()
        if x == 2:
            rot = -1
        else:
            rot = 1
        lock.release()
        Knob.rot = rot
        return 
