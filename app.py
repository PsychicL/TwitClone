from flask import Flask, render_template
from markupsafe import escape
from sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<name>")
def sayhi(name):
    return f"hey {escape(name)}"


if __name__ == "__main__":
    app.run(debug=True)