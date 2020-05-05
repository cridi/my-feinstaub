#!/usr/bin/env python3

import csv
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from datetime import *
from dateutil.tz import *
import numpy as np
import array as arr
import matplotlib

import dateutil.parser

with open('../CSVfiles/Daily/temp_Feinstaub.csv', mode='r') as feinstaub_file:
    feinstaub_reader = csv.DictReader(feinstaub_file, delimiter = ';')

    timeStaub_arr = []
    timeTemp_arr = []
    P1_arr   = []
    P2_arr   = []
    temp_arr = []
    hum_arr  = []

    for row in feinstaub_reader:
        timestamp = dateutil.parser.parse(row["timestamp"])
        timeStaub_arr.append(timestamp)
        P1_arr.append(float(row["P1"]))
        P2_arr.append(float(row["P2"]))

    with open('../CSVfiles/Daily/temp_Temperature.csv', mode='r') as temperature_file:
        temperature_reader = csv.DictReader(temperature_file, delimiter = ';')

        for row in temperature_reader:
            timestamp = dateutil.parser.parse(row["timestamp"])
            timeTemp_arr.append(timestamp)
            temp_arr.append(float(row["temperature"]))
            hum_arr.append(float(row["humidity"]))

    StaubPlot = plt.subplot2grid((2,1),(0,0))
    TempPlot  = plt.subplot2grid((2,1),(1,0))

    #10:10 Wasser hingestellt

    formatter = mdates.ConciseDateFormatter(timeStaub_arr)
    #Oben
    StaubPlot.set_title(" FeinStaub 10/2,5µm ")
    StaubPlot.xaxis.set_major_formatter(formatter)
    StaubPlot.plot(timeStaub_arr, P1_arr, 'm' )
    StaubPlot.plot(timeStaub_arr, P2_arr, 'c')
    StaubPlot.grid(True)

    #Unten
    TempPlot.set_title(" Temperature & Humidity " )
    TempPlot.xaxis.set_major_formatter(formatter)
    TempPlot.plot(timeTemp_arr, temp_arr, 'r')
    TempPlot.plot(timeTemp_arr, hum_arr)
    TempPlot.grid(True)

    plt.show()
