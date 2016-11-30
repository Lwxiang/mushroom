# -*- coding: utf-8 -*-


# Deluge Settings

DELUGE_COMMAND = 'deluge-console'

INFO_HEADS = (
    'Name',
    'ID',
    'State',
    'Seeds',
    'Size',
    'Seed time',
    'Tracker status',
    'Progress',
)

INFO_SPLIT = "\r\n"

# Server Settings

URL = "http://127.0.0.1:8000/monitor/"

HEADER = {
    'content-type': 'application/json'
}
