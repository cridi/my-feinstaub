#!/usr/bin/env python3

import os

os.system("python3 getYesterdaysData.py")
os.system("python3 prepareData.py noShow")
os.system("python3 sendMail.py")
