# -*- coding: utf-8 -*-
import os

import requests

from operate import Deluge
from settings import URL, HEADER


def post_data(data):
    r = requests.post(url=URL, json=data)
    print r


def main():
    deluge = Deluge()

    while True:
        deluge.get_info()
        post_data(deluge.data)
        break


if __name__ == "__main__":
    main()