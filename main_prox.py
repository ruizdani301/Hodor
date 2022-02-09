#!/usr/bin/python3
"""call class
"""
proxy = __import__('proxis').Proxi


new1 = proxy()

for ip in  new1.get_proxi():
    print(ip)
