from flask import Flask

app = Flask(__name__)

@app.route('/<:userid>')
def hello(userid):
    return 'hello world id = {}'.format(userid)

@app.route('/text1')
def text():
    return "text!"

if __name__ == '__main__':
    app.debug = True
    app.run("127.0.0.1",port=5000)