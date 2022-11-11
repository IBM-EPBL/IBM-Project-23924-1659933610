from flask import Flask, render_template, redirect
import ibm_db

app = Flask(__name__)

@app.route("/authentication")
def auth():
    return render_template('auth.html')

@app.route("/news")
def display_news():
    return render_template('news.html')


@app.route("/logout")
def logout():
    return redirect('/authentication')

if __name__ == "__main__":
    app.run()