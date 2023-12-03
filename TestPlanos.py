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


# sleep_time = 0.033 # approx 30fps
# sleep_time = 0.017 # approx 60fps = 0.017
sleep_time = 0.1

NUMBEROFLEDS = 750
pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS, auto_write=False, pixel_order=neopixel.RGB)

csvFile = sys.argv[1]
print(csvFile)

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
        rgb_tuples = [(numbers[i], numbers[i+1], numbers[i+2]) for i in range(0, len(numbers), 3)]
        lightArray.append(rgb_tuples)
print("Finished Parsing")

# run the code on the tree
ciclo=0
while True:
    for n, frame in enumerate(lightArray):
        print("running frame " + str(n))
        LED = 0
        while LED < NUMBEROFLEDS:
            pixels[LED] = frame[LED]
            LED += 1
        pixels.show()
        time.sleep(sleep_time)
    ciclo +=1

    print(f'Cilo terminado ({ciclo})')
#        time.sleep(sleep_time)
