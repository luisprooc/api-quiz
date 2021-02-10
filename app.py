from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/quiz.db'
db = SQLAlchemy(app)


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(20), unique=False, nullable=False)
    correct_answer = db.Column(db.String(70), unique=True, nullable=False)
    incorrect = db.Column(db.String(70), unique=False, nullable=False)
    incorrect2 = db.Column(db.String(70),unique=False, nullable=False)


@app.route('/quiz')
def quiz():
    return 'Hello World!'

@app.route('/new',methods=["POST"])
def new():
    try:
        new = Quiz(question="Se refiere al acto de transferir un archivo o fichero desde un servidor a nuestro computador:",category="Tecnologia",correct_answer="Dowload.",incorrect="Upload.",incorrect2="Transfer.")
        db.session.add(new)
        db.session.commit()
        return 'Question ADDED'

    except:
        return "ERROR"

if __name__ == '__main__':
    app.run(debug=True,port=5000)