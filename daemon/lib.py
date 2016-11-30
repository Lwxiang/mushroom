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
            data.append(single)
            single = {}
            continue

        if raw_cell.startswith('Name'):
            single['Name'] = raw_cell[6:]
        elif raw_cell.startswith('ID'):
            single['ID'] = raw_cell[4:]
        elif raw_cell.startswith('State'):
            state = raw_cell.split(' ')[1]
            single['State'] = state
            if state == 'Downloading':
                speed = raw_cell.split(' ')
                single['SpeedDown'] = speed[4] + ' ' + speed[5]
                single['SpeedUp'] = speed[8] + ' ' + speed[9]
        elif raw_cell.startswith('Seeds'):
            point = raw_cell.split(' ')
            single['Seeds'] = point[1] + ' ' + point[2]
            single['Peers'] = point[4] + ' ' + point[5]
            single['Availability'] = point[7]
        elif raw_cell.startswith('Size'):
            size = raw_cell.split(' ')
            single['Size'] = size[1] + ' ' + size[2] + ' ' + size[3]
            single['Ratio'] = size[5]
        elif raw_cell.startswith('Seed time'):
            seed_time = raw_cell.split(' ')
            single['SeedTime'] = seed_time[2] + ' ' + seed_time[3] + ' ' + seed_time[4]
            single['Active'] = seed_time[6] + ' ' + seed_time[7] + ' ' + seed_time[8]
        elif raw_cell.startswith('Tracker status'):
            single['Tracker'] = raw_cell[16:]
        elif raw_cell.startswith('Progress'):
            single['Progress'] = raw_cell.split(' ')[1]

    return reversed(data)
