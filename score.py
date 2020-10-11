import time
from pycricbuzz import Cricbuzz
import twitter
import random
import requests
import os

os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

print(os.environ['http_proxy'])
print(os.environ['https_proxy'])


extra_words = ['Wow!!', 'amazing!', 'Good stuff!', 'Greatttt one', 'Superb!', '', 'Evergreen shot!', 'Niceeee','Woahhh','Stunner', 'Perfect', 'Unreal!!', "\U0001F618", "\U0001F607", "\U0001F49D", "\U0001F49A", "\U0001F4AB"]
smileys = ["\U0001F973", "\U0001F60E", "\U0001F917", "\U0001F60D", "\U0001F970", "\U0001F929", "\U0001F618", "\U0001F607", "\U0001F49D", "\U0001F49A", "\U0001F4AB", "\U0001F44C", "\U0001F91F", "\U0001F44F", "\U0001F483", "\U0001F57A"]


c = Cricbuzz()

matches = c.matches()


for i in matches:
    if  i['srs'] == 'Indian Premier League 2020':
        print(i)
        mid = i['id']
        print(mid)


while True:

    with open('E:/dummy.txt', 'r') as f:
        content = f.read()

    xxx,yyy = content.split(' ')
    total_fours=int(xxx)
    total_sixes=int(yyy)

    scard = c.scorecard(mid)

    x = scard['scorecard']
    print(x)

    for i in x:

        fours = 0
        sixes = 0

        print("Over is less than 6.0 "+ str(i['overs']))
        
        if float(i['overs']) <= 6.0:
            for j in i['batcard']:
                fours = fours + int(j['fours'])
                sixes = sixes + int(j['six'])

            four_diff = fours - total_fours
            six_diff = sixes - total_sixes

            if four_diff > 0 or six_diff > 0:

                if four_diff > 0:
                    api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                      consumer_secret=os.environ.get('CONSUMER_SECRET'),
                      access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                      access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'))
                    
                    # status = api.PostUpdate('Over: ' + i['overs'] + ' - 4/Four! '
                    #                         + random.choice(extra_words) + random.choice(smileys) + random.choice(
                    #     smileys) + '\n'
                    #                         + "#PowerplayWithChampions " + "#Powerplay "+ "@flipkartvideo")
                    # print("Tweeted as " + status.text)
                    # api=[]
                    print("Four")                

                if six_diff > 0:
                    api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                      consumer_secret=os.environ.get('CONSUMER_SECRET'),
                      access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                      access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'))
                    
                    # status = api.PostUpdate('Over: ' + i['overs'] + ' - 6/Six! '
                    #                         + random.choice(extra_words) + random.choice(smileys) + random.choice(
                    #     smileys) + '\n'
                    #                         + "#PowerplayWithChampions " + "#Powerplay " + "@flipkartvideo")
                    # print("Tweeted as " + status.text)
                    # api=[]

                    print("Six"))

                total_fours = fours
                total_sixes = sixes

                content_to_write = str(total_fours)+" "+str(total_sixes)

                with open('E:/dummy.txt','w') as w:
                    w.write(content_to_write)
        else:

            if total_fours != 0 or total_sixes != 0:        # Reset file when overs greater than 6.0

                content_to_write = "0 0"


                with open('dummy.txt', 'w') as w:
                    w.write(content_to_write)
                print("File reset done")
                                              
    time.sleep(30)

 
