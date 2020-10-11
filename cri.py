import time
import requests
import json
import re
import os

proxyDict = {
    "http"  : os.environ.get('FIXIE_URL', ''),
    "https" : os.environ.get('FIXIE_URL', '')
}

print(proxyDict)

print(requests.head('http://mapps.cricbuzz.com/cbzios/match/livematches').headers)

xx = requests.get('http://mapps.cricbuzz.com/cbzios/match/livematches', proxies=proxyDict)

print(xx)
print(xx.text)
print(xx.json())
