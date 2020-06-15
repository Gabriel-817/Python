# 파일명 : flask01.py

from flask import Flask, render_template, request, redirect

import cx_Oracle as oci  # pip install cx_oracle

# 아이디/암호@서버주소:포트번호/SID
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

app = Flask(__name__)

@app.route("/")                   #화면 페이지 만드는 법
def index():
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall() # [(    ),(    ),(    )]
    return render_template('list.html', list=data)
    print(type(data))
    print(data)

    return "index page"

@app.route("/join", methods=['GET'])
def join():
    return render_template('join.html')

@app.route("/join", methods=['POST'])
def join_post():
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name'] 
    d = request.form['age']
    #print("{}:{}:{}:{}".format(a,b,c,d))
    sql = "INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)"

    cursor.execute(sql, id=a, pw=b, na=c, ag=d)
    conn.commit()

    # 오라클 DB접속
    # 추가하는 SQL문 작성 => INSERT, SELECT, UPDATE, DELETE
    # SQL문 수행

    return redirect('/') #127.0.0.1:5000/
    #127.0.0.1/ 크롬에서 입력한 것처럼 동작
    
@app.route("/login", methods=['GET'])
def login_post():
    print("login-post")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
