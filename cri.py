import time
import requests
import json
import re

try:
    xx = requests.get('http://mapps.cricbuzz.com/cbzios/match/livematches')
    print(xx)
    print(xx.text)
    print("************************************")

except:
    pass

x = requests.get('http://mapps.cricbuzz.com/cbzios/match/livematches')
print(x)
resp_parsed = re.sub(r'^jsonp\d+\(|\)\s+$', '', x.text)

print("*****************************")
print(resp_parsed)

data = json.loads(resp_parsed)
print(data)
