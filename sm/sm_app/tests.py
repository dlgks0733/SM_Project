from django.test import TestCase
from pymongo import MongoClient
import requests
import json
import schedule
import time
# Create your tests here.

### auth - LEE HAN
### 데이터 요청 후 JSON loads
def requestData(urlText):
    data = json.loads(urlText)
    pages = data['totalPages']
    json_str = json.dumps(data)
    data2 = json.loads(json_str)

    return data2, pages

### auth - KIM JONG UK, LEE HAN
### MongoDB 연결 후 데이터 저장
def dbTest():
    conn = MongoClient('127.0.0.1')

    db = conn.test_db
    collect = db.collect

    urlStr = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page='
    url = requests.get(urlStr.__add__('1'))

    (data2, pages) = requestData(url.text)
    collect.insert(data2)

    i = 2
    for i in range(i, pages+1):
        url = requests.get(urlStr.__add__(i.__str__()))
        (data2, temp) = requestData(url.text)
        collect.insert(data2)
     

   
    print('Insert Success')

### auth - LEE HAN
### 1시간 단위 스케줄러 (추후 개발)
# def testScheduler():  
#     print('Working...')

# schedule.every(5).seconds.do(testScheduler)  

# while 1:  
#     schedule.run_pending()  
#     time.sleep(1)