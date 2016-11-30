# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

try:
    from listener.settings import search_url
except ImportError:
    search_url = u"http://www.torrentkittyjx.org/"


def get_magnet_from_keyword(keyword):
    url = search_url + u's/' + keyword
    r = requests.get(url=url)
    soup = BeautifulSoup(r.content)
    a = soup.article.find_all('a')
    if len(a) == 0:
        return ''
    try:
        target = a[0]['href']
        url2 = search_url + target
        r2 = requests.get(url=url2)
        soup2 = BeautifulSoup(r2.content)
        target = soup2.find(id="magnetLink").text
        return target
    except (Exception,):
        return ''


def test():
    keyword = u'航海王'
    print get_magnet_from_keyword(keyword)


if __name__ == '__main__':
    test()
