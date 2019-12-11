from flask import Flask

# Applications that will serve the website
app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return 'Hello Flask!'

@app.route('/about')
def about():
    return 'This is a url shortener'
