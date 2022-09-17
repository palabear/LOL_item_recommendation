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

game_data = pd.read_csv('gameid.csv')


print(game_data)

