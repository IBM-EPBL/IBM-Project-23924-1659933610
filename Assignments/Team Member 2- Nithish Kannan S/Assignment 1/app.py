from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=['GET',"POST"])
def hello_world():
    if request.method == "POST":
        name = request.form["usr_name"]
        email = request.form["email"]
        ph = request.form["ph"]
        return "Name:" + name +"\nEmail:" + email + "\nPhone Number:" + str(ph)
    return render_template("reg.html")

if __name__ == '__main__':
	app.run()
