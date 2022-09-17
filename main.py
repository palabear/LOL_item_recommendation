import requests
from urllib import parse
import pprint
import requests
import json
import time
import csv

import pandas as pd

# for문 진행률 확인 라이브러리
from tqdm import tqdm
pp = pprint.PrettyPrinter(indent=4)

api_key = 'RGAPI-a0db683c-78a3-4efd-9cdb-2aa0352e7062'
request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-a0db683c-78a3-4efd-9cdb-2aa0352e7062"
}

def summoner_v4_by_summoner_name(summonerName):
    encodingSummonerName = parse.quote(summonerName)
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{encodingSummonerName}"
    return requests.get(url, headers=request_header).json()

url = 'https://kr.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key=' + api_key

summonerId = {}

r = requests.get(url)
r = r.json()['entries'] #소환사의 고유 id
# print(r.json())

num = 0
for i in r:


    #print(i)
    #print(i['summonerId'], i['summonerName'])
    summonerId[i['summonerName']] = i['summonerId']

    num += 1
print(num)
#print(summonerId.values())
#print(zip(tqdm(summonerId.values()), summonerId.keys()))
accountId = {}

"""
for i, j in zip(tqdm(summonerId.values()), summonerId.keys()):
    url2 = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/' + i + '?api_key=' + api_key
    r = requests.get(url2)

    if r.status_code == 200:  # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif r.status_code == 429:
        print('api cost full : infinite loop start')
        print('loop location : ', i)
        start_time = time.time()

        while True:  # 429error가 끝날 때까지 무한 루프
            if r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(url2)
                print(r.status_code)

            elif r.status_code == 200:  # 다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break

    r = r.json()['accountId']
    print(r)
    accountId[j] = r
    gameId = []
"""
for i, j in zip(tqdm(summonerId.values()), summonerId.keys()):
    url2 = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/' + i + '?api_key=' + api_key
    r = requests.get(url2)

    if r.status_code == 200:  # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif r.status_code == 429:
        print('api cost full : infinite loop start')
        print('loop location : ', i)
        start_time = time.time()

        while True:  # 429error가 끝날 때까지 무한 루프
            if r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(url2)
                print(r.status_code)

            elif r.status_code == 200:  # 다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break

    r = r.json()['accountId']
    print(r)
    accountId[j] = r


    # url3 = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/hqMv8JiT0hjKc96iqUz9ucXFPgsENmbI_5OHPmlyVOCZxwE?queue=420&api_key=RGAPI-e456f533-671c-4947-b960-98443960695b'
print(accountId)
puuid = []
for i in tqdm(accountId.values()):
    url3 = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-account/' + i + '?&api_key=' + api_key
    r = requests.get(url3)

    if r.status_code == 200:  # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif r.status_code == 429:
        print('api cost full : infinite loop start')
        print('loop location : ', i)
        start_time = time.time()

        while True:  # 429error가 끝날 때까지 무한 루프
            if r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(url2)
                print(r.status_code)

            elif r.status_code == 200:  # 다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break
    try:
        r = r.json()['puuid']
        puuid.append(r)
        print("accountID: " + i)
    except:
        print(r.text)
        print('matches 오류 확인불가')
print(puuid)

gameId=[] #puuid를 활용하여 match정보 파악
for i in tqdm(puuid):
    #https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/9EixO7KWNYzL1wcUyCey7Lt7S565EJbw9FX-xdmTvjPBxABj26U-ivjR3lj209x-T7BYw5NJRgAHAw/ids?start=0&count=20
    url3 = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + i + '/ids?type=ranked&start=0&count=20&api_key=' + api_key
    r = requests.get(url3)

    if r.status_code == 200:  # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif r.status_code == 429:
        print('api cost full : infinite loop start')
        print('loop location : ', i)
        start_time = time.time()

        while True:  # 429error가 끝날 때까지 무한 루프
            if r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(url3)
                print(r.status_code)

            elif r.status_code == 200:  # 다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break
    try:
        r = r.json()
        for j in r:
            print(j)
            gameId.append(j)
    except:
        print(i)
        print(r.text)
        print('matches 오류 확인불가')

print(gameId)

with open("gameid.csv", 'w') as file:
  writer = csv.writer(file)
  writer.writerow(gameId)


"""
for i in tqdm(accountId.values()):
    url3 = 'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/' + i + '?queue=420&api_key=' + api_key
    r = requests.get(url3)

    if r.status_code == 200:  # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif r.status_code == 429:
        print('api cost full : infinite loop start')
        print('loop location : ', i)
        start_time = time.time()

        while True:  # 429error가 끝날 때까지 무한 루프
            if r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(url2)
                print(r.status_code)

            elif r.status_code == 200:  # 다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break
    try:
        r = r.json()['matches']

        for j in r:
            j = j['gameId']
            gameId.append(j)
    except:
        print(i)
        print(r.text)
        print('matches 오류 확인불가')

print(len(gameId))
set_gameId = set(gameId)
set_gameId = list(set(gameId))

match_grandmaster = pd.DataFrame(
    columns=['teamId', 'win', 'firstBlood', 'firstTower', 'firstInhibitor', 'firstBaron', 'firstDragon',
             'firstRiftHerald', 'towerKills', 'inhibitorKills', 'baronKills', 'dragonKills', 'riftHeraldKills',
             'gameId'])

wait_num = []

for i in range(len(set_gameId)):
    if i % 30 == 0:
        wait_num.append(i)
num = 0

for i in tqdm(set_gameId[9991:]):
    num += 1

    if num % 30 == 0:
        print("wait_time")
        time.sleep(60)

    url4 = 'https://kr.api.riotgames.com/lol/match/v4/matches/' + str(i) + '?api_key=' + api_key
    r = requests.get(url4)

    if r.status_code == 200:  # response가 정상이면 바로 맨 밑으로 이동하여 정상적으로 코드 실행
        pass

    elif r.status_code == 429:
        print('api cost full : infinite loop start')
        print('loop location : ', i)
        start_time = time.time()

        while True:  # 429error가 끝날 때까지 무한 루프
            if r.status_code == 429:

                print('try 10 second wait time')
                time.sleep(10)

                r = requests.get(url2)
                print(r.status_code)

            elif r.status_code == 200:  # 다시 response 200이면 loop escape
                print('total wait time : ', time.time() - start_time)
                print('recovery api cost')
                break

    try:
        r = r.json()['teams']
        r = r[0]

        input_data = {
            'teamId': r['teamId'],
            'win': r['win'],
            'firstBlood': r['firstBlood'],
            'firstTower': r['firstTower'],
            'firstInhibitor': r['firstInhibitor'],
            'firstBaron': r['firstBaron'],
            'firstDragon': r['firstDragon'],
            'firstRiftHerald': r['firstRiftHerald'],
            'towerKills': r['towerKills'],
            'inhibitorKills': r['inhibitorKills'],
            'baronKills': r['baronKills'],
            'dragonKills': r['dragonKills'],
            'riftHeraldKills': r['riftHeraldKills'],
            'gameId': i
        }

        match_grandmaster = match_grandmaster.append(input_data, ignore_index=True)

    except:
        print("403 에러..?")

match_grandmaster.to_csv("new_match_grandmaster2.csv", header=False, index=False)
print(match_grandmaster[:45719])
# print
match_grandmaster[:45720].to_csv("new_match_grandmaster2.csv", header=False, index=False)
"""