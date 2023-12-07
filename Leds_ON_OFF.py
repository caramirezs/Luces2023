# Based on code from https://github.com/standupmaths/xmastree2020
import board
import neopixel
import time
from csv import reader
import sys
import time


def ledsOFF(n_leds=750):
    NUMBEROFLEDS = n_leds
    pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS, auto_write=False,
                               pixel_order=neopixel.RGB, brightness=0.7)
    print('Apagar LEDS')
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(1)
    print('proceso terminado')


def ledsON(n_leds=750):
    NUMBEROFLEDS = n_leds
    pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS, auto_write=False,
                               pixel_order=neopixel.RGB, brightness=0.7)
    print('Prender LEDS')
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.1)
    pixels.fill((255, 255, 255))
    pixels.show()
    time.sleep(1)
    print('proceso terminado')


swtich = sys.argv[1]
try:
    n_leds = int(sys.argv[2])
except:
    n_leds = 750

if swtich == "ON":
    ledsOFF()
    ledsON(n_leds)
elif swtich == "OFF":
    ledsOFF(n_leds)
