#import time
#import requests
#import json
#import re

#import os
#import requests

#os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
#os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

print("++++++++++++++++++++++")
#xx = requests.get('http://mapps.cricbuzz.com/cbzios/match/livematches')

#print(xx)
#print(xx.text)
#print(xx.json())


with open('dummy.txt', 'r') as f:
        content = f.read()

print(content)
