from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import session





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)
app.secret_key = b'sSA!)-.-)_+<%!!-_+*@w21R'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<name>")
def sayhi(name):
    return f"hey {escape(name)}"

@app.route("/signup",methods = ['POST', 'GET'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST": 
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index", id=user.id))

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        user = User.query.filter_by(username=request.form["username"], password=request.form["password"]).first()
        if user:
            session['id'] = user.id
            return redirect(url_for("index"))
        else:
            return redirect("/loginerror")
        
@app.route("/loginerror")
def loginerror():
    return render_template("loginerror.html")

db.init_app(app)
if __name__ == "__main__":
    app.run(debug=True)