import time
import requests
import json
import re

import os
import requests


proxies = {'http': "socks5://" + os.environ['IPB_SOCKS5'],
           'https': "socks5://" + os.environ['IPB_SOCKS5'] }

print(proxies)

response = requests.get('http://ifconfig.co', proxies=proxies)
print response.content

response = requests.get('http://google.com', proxies=proxies)
print response.text


print("++++++++++++++++++++++")
xx = requests.get('http://mapps.cricbuzz.com/cbzios/match/livematches')

print(xx)
print(xx.text)
print(xx.json())
