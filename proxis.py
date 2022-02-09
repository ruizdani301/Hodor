#!/usr/bin/python3
"""Initialization module
"""


from bs4 import BeautifulSoup
import requests


class Proxi():

    def __init__(self, url="https://www.free-proxy-list.net/"):
        self.url = url

    @property
    def url(self):
        """update url
        """
        return self.__url

    @url.setter
    def url(self, url):
        """update url
        """
        self.__url = url

    def get_proxi(self):
        html = requests.get(self.__url)
        soup = BeautifulSoup(html.text, "html.parser")
        result = soup.find("tbody").find_all("tr")
        list_proxy = []
        for line in result:
            list_proxy.append(line.find("td").text)

        return list_proxy
