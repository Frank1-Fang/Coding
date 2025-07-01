from flask import Flask

app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000/
def home():
    return 'Welcome to the Home Page!'

@app.route('/about') # http://127.0.0.1:5000/about
def about():
    return 'This is the About Page.'

if __name__ == '__main__':
    app.run(debug=True)
