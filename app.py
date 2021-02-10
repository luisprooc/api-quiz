from flask import Flask
app = Flask(__name__)

@app.route('/quiz')
def quiz():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True,port=5000)