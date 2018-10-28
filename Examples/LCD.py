#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi

import datetime
from time import sleep
import Adafruit_CharLCD as LCD


# Raspberry Pi pin setup
lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 0
lcd_backlight = 1

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4,
 lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

date = str(datetime.date.today()).split('-')
t = str(datetime.datetime.now().time()).split(':')

try:
    print('Ready')
    
    lcd.message('   {}/{}/{}'.format(date[1],date[2],date[0]))
    lcd.message('\n    {}:{}:{:.2}'.format(t[0],t[1],t[2]))

    while True:
        t= str(datetime.datetime.now().time()).split(':')
        lcd.clear()
        lcd.message('   {}/{}/{}'.format(date[1],date[2],date[0]))
        lcd.message('\n    {}:{}:{:.2}'.format(t[0],t[1],t[2]))
        sleep(.5)

except KeyboardInterrupt:
    lcd.clear()
