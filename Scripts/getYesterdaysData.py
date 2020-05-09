#!/usr/bin/env python3


from datetime import date
from datetime import timedelta

import urllib.request as urlget
import os
import shutil
import sys

def get( year, month, day ):

    print( os.path.abspath(__file__) )

    urlFeinstaubSensData    = 'http://archive.luftdaten.info/' + year + '-' + month + '-' + day + '/' + year + '-' + month + '-' + day + '_sds011_sensor_45534_indoor.csv'
    urlTemperatureSensData  = 'http://archive.luftdaten.info/' + year + '-' + month + '-' + day + '/' + year + '-' + month + '-' + day + '_dht22_sensor_45535_indoor.csv'

    print(urlFeinstaubSensData)
    print(urlTemperatureSensData)

    # Copy a network object to a local file

    urlget.urlretrieve(urlFeinstaubSensData,   ( "../CSVfiles/Daily/temp_Feinstaub.csv" ) )
    urlget.urlretrieve(urlTemperatureSensData, ( "../CSVfiles/Daily/temp_Temperature.csv" ) )

    shutil.copyfile( "../CSVfiles/Daily/temp_Feinstaub.csv",    ( "../CSVfiles/Daily/" + year + '-' + month + '-' + day + "_Feinstaub.csv" ) )
    shutil.copyfile( "../CSVfiles/Daily/temp_Temperature.csv" , ( "../CSVfiles/Daily/" + year + '-' + month + '-' + day + "_Temperature.csv" ) )
