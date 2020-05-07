#!/usr/bin/env python3


from datetime import date
from datetime import timedelta

import urllib.request as urlget
import os
import shutil


#Get todays Date
today = date.today()
print("Today's date:", today)

# Yesterday date
yesterday = today - timedelta(days = 1)
print("Yesterday was: ", yesterday)

#Adjust to linkformat
year  = str(yesterday.year)
month = str(yesterday.month) if yesterday.month >= 10 else "0"+str(yesterday.month)
day   = str(yesterday.day)   if yesterday.day   >= 10 else "0"+str(yesterday.day)

urlFeinstaubSensData    = 'http://archive.luftdaten.info/' + year + '-' + month + '-' + day + '/' + year + '-' + month + '-' + day + '_sds011_sensor_45534_indoor.csv'
urlTemperatureSensData  = 'http://archive.luftdaten.info/' + year + '-' + month + '-' + day + '/' + year + '-' + month + '-' + day + '_dht22_sensor_45535_indoor.csv'

print(urlFeinstaubSensData)
print(urlTemperatureSensData)

# Copy a network object to a local file

urlget.urlretrieve(urlFeinstaubSensData,   ( "../CSVfiles/Daily/temp_Feinstaub.csv" ) )
urlget.urlretrieve(urlTemperatureSensData, ( "../CSVfiles/Daily/temp_Temperature.csv" ) )

shutil.copyfile( "../CSVfiles/Daily/temp_Feinstaub.csv",    ( "../CSVfiles/Daily/" + year + '-' + month + '-' + day + "_Feinstaub.csv" ) )
shutil.copyfile( "../CSVfiles/Daily/temp_Temperature.csv" , ( "../CSVfiles/Daily/" + year + '-' + month + '-' + day + "_Temperature.csv" ) )


#os.remove('tempFeinstaub.csv')
#os.remove('tempTemperature.csv')
