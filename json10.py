import pymongo
import requests
import json

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") # 없으면 db1생성
table = db.get_collection("exam10") #collection 생성

url = "http://ihongss.com/json/exam10.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict
"""
[
    {'id': "id1", 'name': '가나다1', 'age': 31 
        'score':{
            math:[50], 
            kor: [69]
            }      
        },
    {'id': "id2", 'name': '가나다2', 'age': 32 
        'score':{
            math:[90], 
            kor: [80]
            }      
        },
    {'id': "id3", 'name': '가나다3', 'age': 33 
        'score':{
            math:[70], 
            kor: [60]
            }      
        },
    {'id': "id4", 'name': '가나다4', 'age': 34 
        'score':{
            math:[80], 
            kor: [50]
            }      
        },
    {'id': "id5", 'name': '가나다5', 'age': 35 
        'score':{
            math:[80], 
            kor: [90]
            }      
        }
]
"""
# insert_one({})
# insert_many([{},{},{}])
for tmp in data1['data'] :
    # print(tmp['name'])
    # print(tmp['species'])
    # print(tmp['foods']['likes'][0]) #{ , }
    # print(tmp['foods']['dislikes'][0])
    print(data1)
    dict1 = dict()
    dict1['id'] = tmp['id']
    dict1['name'] = tmp['name']
    dict1['age'] = tmp['age']
    dict1['math'] = tmp['score']['math']
    dict1['kor'] = tmp['score']['kor']
    
    table.insert_one(dict1)

conn.close()