from flask import flask

app = Flask(__main__)

@app.route('/')
def home:
    return "Ciaone"
