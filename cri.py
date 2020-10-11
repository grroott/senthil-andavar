import time
import requests
import json
import re

import os
import requests


os.environ['http_proxy'] = os.environ.get('FIXIE_URL', '')
os.environ['https_proxy'] = os.environ.get('FIXIE_URL', '')


xx = requests.get('http://mapps.cricbuzz.com/cbzios/match/livematches')

print(xx)
print(xx.text)
print(xx.json())
