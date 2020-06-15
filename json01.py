# 파일명 : json01.py
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

# 파일 읽기
file1 = open('./resources/exam2.json')
# str to dict로 변경
data1 = json.load(file1)

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, :PW, :NAME, :AGE, SYSDATE)
    """
cursor.execute(sql, data1)
conn.commit()

# print(data1)
# print(type(data1))