from datetime import timedelta
from flask import Flask,session,render_template,request, redirect
import ibm_db
import setup


app = Flask(__name__)
app.secret_key = "NEWSpro"
app.permanent_session_lifetime = timedelta(days = 10000)

@app.route("/login",methods=('GET','POST'))
def auth():
    
    conn=setup.setupConnection()
    print(conn)
    # conn=setup.conn
    # # setup.createTable(setup.conn)
    if "user" in session:
        return redirect('/news')
    if request.method == "POST":
        email = request.form["loginEmail"]
        pwd = request.form["loginPassword"]
        stmt = ibm_db.exec_immediate(conn,"select * from UserDB")
        while ibm_db.fetch_row(stmt) != False:
            print(ibm_db.result(stmt,1),ibm_db.result(stmt,2))
            if email == ibm_db.result(stmt,1) and pwd == ibm_db.result(stmt,2):
                session.permanent = True
                session["user"] = email
                return redirect('/news')
        return render_template('login.html',message="Record not found. Please check your credentials")
    return render_template('login.html')
    
    # error=None
    # if request.method == 'POST':

    #     username = request.form['loginEmail']
    #     password = request.form['loginPassword']
    #     cred=ibm_db.exec_immediate(setup.conn,"Select password From UserDB Where username = '{}';".format(username))

    #     if cred is None:
    #         error = 'Incorrect Username/Password.'
    #     elif password != ibm_db.result(cred,0):
    #         print(username)
    #         error = 'Incorrect Password.'

    #     if error is None:
    #         return redirect('/news')  
    # return render_template('login.html')

#news
# if "user" not in session:
#         return redirect('/login')

# return render_template('news.html',user_email = session["user"])


@app.route("/news")
def display_news():
    if "user" not in session:
        return redirect('/login')
    return render_template('news.html',user_email = session["user"])


@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user" , None)
    return redirect('/login')

@app.route("/register",methods=('GET','POST'))
def register():
    conn=setup.setupConnection()
    print(conn)
    if "user" in session:
        return redirect('/news')
    if request.method == "POST":
        email = request.form["email"]
        pwd = request.form["pwd"]
        c_pwd = request.form["c_pwd"]
        
        if pwd != c_pwd:
           return render_template('register.html',message="Passwords don't match")

	#check if already present or not
        stmt = ibm_db.exec_immediate(conn,"select * from UserDB;")
        prevId=0
        while ibm_db.fetch_row(stmt) != False:
            prevId=ibm_db.result(stmt,0)
            if email == ibm_db.result(stmt,1):    
                return render_template('register.html',message="An user already exists with this account")	
        print(prevId)
        insertQuery = "insert into UserDB values({},'{}','{}');".format(int(prevId)+1,email,pwd)
        print(insertQuery)
        try:
            insert_table = ibm_db.exec_immediate(conn,insertQuery)
            print(insert_table)
            session.permanent = True
            session["user"] = email
            return redirect('/news')
        except:

            return render_template('register.html',message="An unknown error has occured")


    
    return render_template('register.html')


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 8080, debug = True)