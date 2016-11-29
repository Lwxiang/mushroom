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

    def get_raw_info(self):
        # Get raw string from command line
        process = subprocess.Popen([self.command, "info"], stdout=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        return out

    def get_info(self):
        # Get dict of torrents-info
        return parse_from_deluge_raw(self.get_raw_info())
