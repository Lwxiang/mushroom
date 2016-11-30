# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

from listener.settings import search_url


def get_magnet_from_keyword(keyword, site_url=search_url):
    url = site_url + 's/' + keyword
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text)
    a = soup.article.find_all('a')
    if len(a) == 0:
        return ''
    try:
        target = a['href']
        url2 = site_url + target
        r2 = requests.get(url=url2)
        soup2 = BeautifulSoup(r2.text)
        target = soup2.find(id="magnetLink").text
        return target
    except (Exception,):
        return ''


def test():
    keyword = u'航海王'
    print get_magnet_from_keyword(keyword, "http://www.torrentkittyjx.org/")


if __name__ == '__main__':
    test()
