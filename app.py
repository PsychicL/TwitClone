from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<name>")
def sayhi(name):
    return f"hey {escape(name)}"


if __name__ == "__main__":
    app.run(debug=True)