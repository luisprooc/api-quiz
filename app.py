from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from random import randint

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


@app.route('/quiz/sc',methods=["GET"])
def quiz_sc():
    try:
        science = Quiz.query.filter_by(category = 'Ciencia').all()
        num = randint(1,len(science))
        res = {
            "Id":science[num].id,"Category":science[num].category,
            "Correct":science[num].correct_answer,"Incorrect":science[num].incorrect,
            "Incorrect2":science[num].incorrect2
            }
        return jsonify(res)
    
    except:
        return "Error in GET REQUEST"

@app.route('/quiz/tec',methods=["GET"])
def quiz_tec():
    try:
        tec = Quiz.query.filter_by(category = 'Tecnologia').all()
        num = randint(1,len(tec))
        res = {
            "Id":tec[num].id,"Category":tec[num].category,
            "Correct":tec[num].correct_answer,"Incorrect":tec[num].incorrect,
            "Incorrect2":tec[num].incorrect2
            }
        return jsonify(res)
    
    except:
        return "Error in GET REQUEST"
    



if __name__ == '__main__':
    app.run(debug=True,port=5000)