import sys
import os

main_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(main_path)

from TestPlanos import run_testplanos, run_puntos_region

csvFile = sys.argv[1]
if len(sys.argv) > 2:
    sleep_time = float(sys.argv[2])  # en segundos
else:
    sleep_time = 0.017  # approx 60fps = 0.017
# Fetch & Pull

# run_testplanos(csvFile, sleep_time)

lista_puntos = [1, 2, 3, 6, 7, 10, 11, 12, 13, 15, 16, 17, 18, 21, 25, 26, 27, 28, 29, 31, 33, 34, 36, 37, 39, 40, 41,
                43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 70, 71, 72, 73,
                74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 118, 120, 121, 122, 123, 151, 528, 542, 543,
                544, 545, 546, 548, 549, 550, 552, 553, 562, 564, 565, 566, 567, 568, 572]
run_puntos_region(lista_puntos)
