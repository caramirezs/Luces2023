import sys
import os

main_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(main_path)

from TestPlanos import run_testplanos
csvFile = sys.argv[1]
if len(sys.argv) > 2:
    sleep_time = float(sys.argv[2]) # en segundos
else:
    sleep_time = 0.017 # approx 60fps = 0.017
# Fetch & Pull

run_testplanos(csvFile, sleep_time)


