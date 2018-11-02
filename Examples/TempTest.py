from time import sleep
import Adafruit_CharLCD as LCD
import Adafruit_DHT

#DHT 11 Sensor
DHT = 11
DHT_pin = 11

# LCD
lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 0
lcd_backlight = 1

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4,
 lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

try:
    print('Ready')
    while True:
        TH = Adafruit_DHT.read_retry(DHT,DHT_pin)
        lcd.clear()
        lcd.message('Temp(C):  {}'.format(TH[1]))
        lcd.message('\nHumidity: {}'.format(TH[0]))
        sleep(2)
        
except KeyboardInterrupt:
    lcd.clear()
