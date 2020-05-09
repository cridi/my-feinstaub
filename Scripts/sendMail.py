#!/usr/bin/env python3

import yagmail
from datetime import date
from datetime import timedelta
import sys
import os

def send( year, month, day ):
    print( os.path.abspath(__file__))
    os.chdir(os.path.dirname(sys.argv[0]))

    receiver = "cridi92@web.de"
    body = " "
    filename = "../Graphs/Daily/current_graph.png"

    print("Filename: " + os.path.abspath(filename))

    yag = yagmail.SMTP("klimaupdate@gmail.com")

    yag.send(
        to          = receiver,
        subject     = "Tägliches Klimaupdate "  + year + '-' + month + '-' + day,
        contents    = body,
        attachments = os.path.abspath(filename),
    )

    print("Email sent!")
    print("to: " + receiver)

def main():
    send("2020", "05", "08")

if __name__ == "__main__":
    main()
