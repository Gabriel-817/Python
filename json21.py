import pymongo
import requests
import json

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") # 없으면 db1생성
table = db.get_collection("exam21") #collection 생성

url = "http://ihongss.com/json/exam21.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict

# for tmp in data1['boxOfficeResult']['showRange'] :
#     print(data1)
#     dict1 = dict()
#     dict1['boxOfficeResult'] = tmp['boxOfficeResult']
#     dict1['showRange'] = tmp['boxOfficeResult']['shoeRange']
#     dict1['dailyBoxOfficeList'] = tmp['boxOfficeResult']['dailyBoxOfficeList']
#     dict1['rankOldAndNew'] = tmp['boxOfficeResult']['dailyBoxOfficeList']['rankOldAndNew']
#     dict1['movieNm'] = tmp['boxOfficeResult']['dailyBoxOfficeList']['movieNm']
#     dict1['salesShare'] = tmp['boxOfficeResult']['dailyBoxOfficeList']['salesShare']
#     dict1['salesAcc'] = tmp['boxOfficeResult']['dailyBoxOfficeList']['salesAcc']
#     dict1['scrnCnt'] = tmp['boxOfficeResult']['dailyBoxOfficeList']['scrnCnt']
#     dict1['showCnt'] = tmp['boxOfficeResult']['dailyBoxOfficeList']['showCnt']

#     table.insert_one(dict1)

a = data1['boxOfficeResult']['showRange']
for tmp in data1['boxOfficeResult']['dailyBoxOfficeList'] :
    print(tmp)
    dict1 = dict()
    dict1['showRange'] = a
    dict1['rankOldAndNew'] = tmp['rankOldAndNew']
    dict1['movieNm'] = tmp['movieNm']
    dict1['salesShare'] = tmp['salesShare']
    dict1['salesAcc'] = tmp['salesAcc']
    dict1['scrnCnt'] = tmp['scrnCnt']
    dict1['showCnt'] = tmp['showCnt']

    table.insert_one(dict1)

conn.close()