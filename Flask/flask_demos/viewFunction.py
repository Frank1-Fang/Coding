from flask import request, Flask

app = Flask(__name__)

@app.route('/greet/<name>') # http://127.0.0.1:5000/greet/Hello
                            # Output: Hello, Hello!
def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
