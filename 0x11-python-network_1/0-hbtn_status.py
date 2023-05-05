#!/usr/bin/python3

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response:")
    print("/t- type: {}".format(type(data)))
    print("/t- content: {}".format(data))
    print("/t- utf8 content: {}".format(data.decode('utf-8')))
