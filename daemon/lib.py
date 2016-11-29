# -*- coding: utf-8 -*-

from settings import INFO_HEADS, INFO_SPLIT


def parse_from_deluge_raw(raw):
    """
    Parse data from deluge command feedback of "[command] info"
    :param raw:
    :return: list of torrents-information
    """
    raw_list = raw.split(INFO_SPLIT)
    data = []
    single = {}

    for index, raw_cell in enumerate(raw_list):
        if index == 0:
            continue

        if raw_cell in ["", " "]:
            pass

