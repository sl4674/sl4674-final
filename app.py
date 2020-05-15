

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/classes")
def page1():
    return render_template("classes.html")

@app.route("/assignments")
def page2():
    return render_template("assignments.html")
#start the server
if __name__ == "__main__":
    app.run()