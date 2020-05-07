#!/usr/bin/env python3

import yagmail
from datetime import date
from datetime import timedelta


receiver = "cridi92@web.de"
body = " "
filename = "../Graphs/Daily/current_graph.png"

yag = yagmail.SMTP("cridilicious@gmail.com")


#Get todays Date
today = date.today()
# Yesterday date
yesterday = today - timedelta(days = 1)
#Adjust to linkformat
year  = str(yesterday.year)
month = str(yesterday.month) if yesterday.month >= 10 else "0"+str(yesterday.month)
day   = str(yesterday.day)   if yesterday.day   >= 10 else "0"+str(yesterday.day)


yag.send(
    to          = receiver,
    subject     = "Tägliches Klimaupdate "  + year + '-' + month + '-' + day,
    contents    = body,
    attachments = filename,
)
