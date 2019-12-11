from flask import Flask, render_template, request

# Applications that will serve the website
app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return 'This is a url shortener'

@app.route('/your-url', methods=['GET'])
def your_url():
    return render_template('your_url.html', code=request.args['code'])
