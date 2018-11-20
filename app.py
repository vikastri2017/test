from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/information.html')
def info():
    return "Hello Info!"

if __name__ == '__main__':
    app.run()
