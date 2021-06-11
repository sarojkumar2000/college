
from flask import Flask,render_template,request, redirect, url_for, session
import mysql.connector
db=mysql.connector.connect(host="localhost",user="saroj",passwd="1234",database="saroj")
cur=db.cursor()

app=Flask(__name__)


## This is the main page that renders

@app.route('/')
def hello():
    return render_template("index.html")

    

##  Admin
@app.route('/admin',methods=["GET","POST"])
def admin():
    return render_template("admin.html")
    
@app.route('/admin1',methods=["GET","POST"])
def admin1():
    p=request.form["name"]
    q=request.form["passwd"]
    msg="Enter valid credentials"
    if p=="admin" and q=="123":
        return render_template("admin1.html")
    else:
        return render_template("admin.html",y=msg)

@app.route('/newstudent',methods=["GET","POST"])
def newstudent():
    return render_template("student.html")

## Registering student!

@app.route('/registerstudent',methods=["POST"])
def registerstudent():
    stuname=request.form["name"]
    stubranch=request.form["branch"]
    stuyear=request.form["year"]
    stusection=request.form["section"]
    msg="New student added successfully"
    sql="insert into student(name,branch,year,section) values('{}','{}','{}','{}')".format(stuname,stubranch,stuyear,stusection)
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
    return render_template("admin1.html",y=msg)

## Deleting student!

@app.route('/deletestudent',methods=["GET","POST"])
def deletestudent():
    return render_template("deletestudent.html")
@app.route('/studentdelete',methods=["GET","POST"])
def studentdelete():
    p=request.form["name"]
    if len(p)==0:
        return render_template("deletestudent.html",y="Please enter student name to delete")

    msg1="deleted successfully"
    msg="student not found"
    sql="delete from student where name='{}'".format(p)
    cur.execute(sql)
    db.commit()
    if cur.rowcount<1:
        return render_template("deletestudent.html",y=msg)
    else:
        return render_template("admin1.html",y=msg1)



## student login


@app.route('/studentlog',methods=["GET","POST"])
def studentlog():
    return render_template("studentlog.html")

@app.route('/studentlogin',methods=["GET","POST"])
def studentlogin():
    p=request.form["name"]
    q=request.form["branch"]
    r=request.form["section"]
    cur.execute("Select * from student where name=%s and branch=%s and section=%s",(p,q,r))
    account = cur.fetchone()
    msg="welcome "+p
    if account:
        return render_template("studentlogin.html",msg=msg)
    return render_template("studentlog.html",y="Enter valid details")
        





## Displaying students!



## Creating new teacher
@app.route('/newteacher',methods=["GET","POST"])
def newteacher():
    return render_template("teacher.html")
@app.route('/registerteacher',methods=["POST"])
def registerteacher():
    teaname=request.form["name"]
    teabranch=request.form["branch"]
    teayear=request.form["year"]
    teasubject=request.form["subject"]
    msg="New teacher added successfully"
    sql="insert into teacher(name,branch,year,subject) values('{}','{}','{}','{}')".format(teaname,teabranch,teayear,teasubject)
    cur.execute(sql)
    db.commit()
    return render_template("admin1.html",y=msg)


## Deleting teacher
@app.route('/deleteteacher',methods=["GET","POST"])
def deleteteacher():
    return render_template("deleteteacher.html")




@app.route('/delete',methods=["GET","POST"])

def delete():
    p=request.form["name"]
    if len(p)==0:
        return render_template("deleteteacher.html",y="Please enter teacher name to delete")
    msg1="deleted successfully"
    msg="teacher not found"
    sql="delete from teacher where name='{}'".format(p)
    cur.execute(sql)
    db.commit()
    if cur.rowcount<1:
        return render_template("deleteteacher.html",y=msg)
    else:
        return render_template("admin1.html",y=msg1)





   
    
    
app.run(debug=False,host='0.0.0.0')