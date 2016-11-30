# -*- coding: utf-8 -*-
import subprocess

from lib import parse_from_deluge_raw
from settings import DELUGE_COMMAND


class Deluge(object):
    """
    Deluge Operator
    """
    def __init__(self, command=DELUGE_COMMAND):
        self.command = command
        self.data = []

    def add_new_work(self, magnet):

        # Add a new magnet
        process = subprocess.Popen([self.command, "add", "\"%s\"" % magnet], stdout=subprocess.PIPE, shell=True)
        process.communicate()

        now = len(self.data)
        self.get_info()
        if self.data > now:
            self.data[-1]['magnet'] = magnet
            return True
        return False

    def get_raw_info(self):
        # Get raw string from command line
        process = subprocess.Popen([self.command, "info"], stdout=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        return out

    def get_info(self):
        # Get dict of torrents-info
        data = parse_from_deluge_raw(self.get_raw_info())
        for index, d in enumerate(data):
            if index >= len(self.data):
                self.data.append(d)
                continue
            self.data[index].update(d)
        return self.data

    def update(self, data):
        magnet = data.get('magnet', '')
        operate = data.get('operate', '')
        for d in self.data:
            if d.get('magnet', '') == magnet:
                pass
                return

        if operate == 'Download':
            self.add_new_work(magnet)
