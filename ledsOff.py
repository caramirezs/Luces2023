# Based on code from https://github.com/standupmaths/xmastree2020
import board
import neopixel
import time
from csv import reader
import sys
import time

def run_puntos_region(lista_puntos):
    NUMBEROFLEDS = 750
    pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS, auto_write=False,
                               pixel_order=neopixel.RGB, brightness=0.6)
    print('Apagar LEDS')
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(1)
    print('proceso terminado')
