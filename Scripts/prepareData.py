#!/usr/bin/env python3

import sys
import csv
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from dateutil.tz import *
import numpy as np
import matplotlib
import dateutil.parser
import pytz
import os


print( os.path.abspath(__file__) )

def convert_datetime_timezone(dt, tz1, tz2):
    tz1 = pytz.timezone(tz1)
    tz2 = pytz.timezone(tz2)

    dt = tz1.localize(dt)
    dt = dt.astimezone(tz2)

    return dt

def prepData( year, month, day ):
    print( os.path.abspath(__file__))

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
            timeStaub_arr.append(convert_datetime_timezone(timestamp, 'UTC', 'Europe/Berlin'))
            P1_arr.append(float(row["P1"]))
            P2_arr.append(float(row["P2"]))

        with open('../CSVfiles/Daily/temp_Temperature.csv', mode='r') as temperature_file:
            temperature_reader = csv.DictReader(temperature_file, delimiter = ';')

            for row in temperature_reader:
                timestamp = dateutil.parser.parse(row["timestamp"])
                timeTemp_arr.append(convert_datetime_timezone(timestamp, 'UTC', 'Europe/Berlin'))
                temp_arr.append(float(row["temperature"]))
                hum_arr.append(float(row["humidity"]))

        StaubPlot = plt.subplot2grid((2,1),(0,0))
        TempPlot  = plt.subplot2grid((2,1),(1,0))

        #Oben
        StaubPlot.set_title(" FeinStaub 10/2,5µm ")
        formatter = mdates.ConciseDateFormatter(timeStaub_arr, tz=pytz.timezone('Europe/Berlin') )
        StaubPlot.xaxis.set_major_formatter(formatter)
        StaubPlot.grid(True)

        handleP1, = StaubPlot.plot(timeStaub_arr, P1_arr, 'm' )
        handleP2, = StaubPlot.plot(timeStaub_arr, P2_arr, 'c' )
        StaubPlot.legend((handleP1, handleP2), ('10 µm', '2,5 µm'), loc='upper right')

        #Unten
        TempPlot.set_title(" Temperatur & Feuchte ")
        formatter = mdates.ConciseDateFormatter(timeStaub_arr, tz=pytz.timezone('Europe/Berlin') )
        TempPlot.xaxis.set_major_formatter(formatter)
        TempPlot.grid(True)

        handleTemp, = TempPlot.plot(timeTemp_arr, temp_arr, 'r')
        handleHum,  = TempPlot.plot(timeTemp_arr, hum_arr)
        TempPlot.legend((handleHum, handleTemp), ( 'Feuchte', 'Temperatur'), loc='upper right')


        fig = plt.gcf()
        fig.set_size_inches((11, 8.5), forward=False)
        fig.savefig('../Graphs/Daily/current_graph.png', dpi=200)
        fig.savefig('../Graphs/Daily/' + year + '-' + month + '-' + day + "_graph.png", dpi=200)

        if len(sys.argv) > 1:
            if str(sys.argv[1]) == "show":
                plt.show()
