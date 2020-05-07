#!/usr/bin/env python3

import yagmail

receiver = "cridi92@web.de"
body = ""
filename = "../Graphs/Daily/current_graph.png"

yag = yagmail.SMTP("cridilicious@gmail.com")

yag.send(
    to          = receiver,
    subject     = "Tägliches Klimaupdate",
    contents    = body,
    attachments = filename,
)
