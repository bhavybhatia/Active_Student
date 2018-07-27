import sqlite3
import datetime

name=["Anshul","Bhavy","Ishan","Takveer","Anmol"]
dob=["26/12/1995","22/11/1997","4/12/1998","15/12/1997","14/8/1999"]
ndob=[datetime.datetime.strptime(x,"%d/%m/%Y") for x in dob]
status=[0,1,0,1,0]
s_id=[]
for m in range(1001,1006):
    s_id.append(m)

def create_table():
    db=sqlite3.connect("student.db")
    cur=db.cursor()
    cur.execute("CREATE TABLE data(ids int ,student_name varchar(100),student_dob datetime,student_status int)")
    db.commit()
    db.close()

def insert(ids,student_name,student_dob,student_status):
    db=sqlite3.connect("student.db")
    cur=db.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?,?)",(ids,student_name,student_dob,student_status))
    db.commit()
    db.close()

for i,j,k,l in zip(s_id,name,ndob,status):
    insert(i,j,k,l)

def view():
    db=sqlite3.connect("student.db")
    cur=db.cursor()
    cur.execute("SELECT * FROM data")
    rows=cur.fetchall()
    db.close()
    return rows

print(view())
