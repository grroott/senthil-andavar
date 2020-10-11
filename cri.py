
import time
from pycricbuzz import Cricbuzz

c = Cricbuzz()
matches = c.matches()

print(matches)

for i in matches:
    if  i['srs'] == 'Indian Premier League 2020' and i['mchstate'] == 'inprogress' :
        print(i)
        mid = i['id']
        print(mid)
