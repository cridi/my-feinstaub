#!/usr/bin/env python3

import os
import sys
from datetime import *
import prepareData
import sendMail
import getYesterdaysData

os.chdir(os.path.dirname(sys.argv[0]))

#Get todays Date
today = date.today()
# Yesterday date
yesterday = today - timedelta(days = 1)

#Adjust to linkformat
year  = str(yesterday.year)
month = str(yesterday.month) if yesterday.month >= 10 else "0"+str(yesterday.month)
day   = str(yesterday.day)   if yesterday.day   >= 10 else "0"+str(yesterday.day)


print(yesterday)
print('Call getYesterdaysData')
getYesterdaysData.get( year, month, day )
print('Call preData')
prepareData.prepData( year, month, day )
print('Call Send')
sendMail.send( year, month, day )
