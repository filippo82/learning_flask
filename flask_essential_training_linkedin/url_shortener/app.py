from flask import Flask, render_template

# Applications that will serve the website
app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('home.html', name='Filippo')

@app.route('/about')
def about():
    return 'This is a url shortener'
