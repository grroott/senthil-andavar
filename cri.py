import time
import requests
import json
import re

import os
import requests

os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')



response = requests.get('http://ifconfig.co)
print(response)
response = requests.get('https://www.google.com')
print(response)


print("++++++++++++++++++++++")
xx = requests.get('http://mapps.cricbuzz.com/cbzios/match/livematches')

print(xx)
print(xx.text)
print(xx.json())
