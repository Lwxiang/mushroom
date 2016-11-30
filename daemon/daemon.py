# -*- coding: utf-8 -*-
from time import sleep

import requests

from operate import Deluge
from settings import URL, HEADER


def post_data(data):
    r = requests.post(url=URL, json=data)
    return r.json()


def main():
    deluge = Deluge()

    while True:
        deluge.get_info()
        result_data = post_data(deluge.data)
        if result_data.get('result', False):
            data = result_data.get('data', [])
            for d in data:
                deluge.update(d)
        sleep(5)


if __name__ == "__main__":
    main()
