# (c) 2020, Lucas Benedito <llucasdias@icloud.com>

import os


def calc_fuel(stintTime, lapTime, fuelLap, tankCap):
    lapsAvg = stintTime / lapTime
    fuelTotal = lapsAvg * fuelLap
    pitTotal = fuelTotal / tankCap
    print(f"Your calculated fuel is: %.0fL | Total Laps: %.0f | Pitstops Needed: %.0f" % (fuelTotal, lapsAvg, pitTotal))
