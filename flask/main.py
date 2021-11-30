import flask
from flask import *
import winsound
app = Flask(__name__)
@app.route("/")
def redirect_to_login():
    return redirect(url_for("login"))



@app.route("/home<name>",methods=["POST", "GET"])
def home(name):
    if request.method == "POST":
         if "logout" in request.form:
             return  redirect(url_for("login"))
            
    return render_template("home.html",name = name)
 
    

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("home",name = user))
    return render_template("login.html")
    
@app.route("/home",methods=["POST", "GET"])
def home2():
    return render_template("home.html",name = "user")
    

if __name__ == "__main__":
     app.run()
     
