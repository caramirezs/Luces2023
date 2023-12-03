# Based on code from https://github.com/standupmaths/xmastree2020
import board
import neopixel
import time
from csv import reader
import sys
import time


# helper function for chunking
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def run_testplanos(csvFile, sleep_time):
    print(csvFile)
    NUMBEROFLEDS = 750
    pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS, auto_write=False,
                               pixel_order=neopixel.RGB, brightness=0.6)

    # read the file
    # iterate through the entire thing and make all the points the same colour
    lightArray = []
    with open(csvFile, 'r', newline='') as file:
        # pass the file object to reader() to get the reader object
        reader_file = reader(file)
        next(reader_file)  # Skip the header
        # Iterate over each row in the csv using reader object
        for row in reader_file:
            # row variable is a list that represents a row in csv
            # break up the list of rgb values
            row.pop(0)
            numbers = list(map(int, row))
            rgb_tuples = [(numbers[i], numbers[i + 1], numbers[i + 2]) for i in range(0, len(numbers), 3)]
            lightArray.append(rgb_tuples)
    print("Finished Parsing")

    # run the code on the tree
    ciclo = 0
    while True:
        for n, frame in enumerate(lightArray):
            print("running frame " + str(n))
            LED = 0
            while LED < NUMBEROFLEDS:
                pixels[LED] = frame[LED]
                LED += 1
            pixels.show()
            time.sleep(sleep_time)
        ciclo += 1
        print(f'Cilo terminado ({ciclo})')


def run_puntos_region(lista_puntos):
    NUMBEROFLEDS = 750
    pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS, auto_write=False,
                               pixel_order=neopixel.RGB, brightness=0.6)
    print('LEDS encendidos')
    pixels.fill((0, 50, 0))
    pixels.show()
    time.sleep(1)
    while True:
        for i in lista_puntos:
            pixels[i] = (0, 0, 50)
        pixels.show()

        for i in lista_puntos:
            print(f'Prendiendo pixel {i}')
            pixels[i] = (100, 0, 0)
            pixels.show()
            input('continuar?')
