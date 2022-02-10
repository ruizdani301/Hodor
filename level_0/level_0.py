#!/usr/bin/python3

import requests

data_form = {"id": "3819", "holdthedoor": "Submit"}

if __name__ == "__main__":
    i = 0
    while (i != 1024):
        new_date = requests.post("http://158.69.76.135/level0.php", data=data_form)
        i = i + 1
