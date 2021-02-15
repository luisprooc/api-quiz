import re
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from random import randint
from flask_cors import CORS

app = Flask(__name__)


# CORS

CORS(app)
cors = CORS(app, resources={
    r"/*" :{
        "origin": "*"
    }
})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/quiz.db'
db = SQLAlchemy(app)


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(20), unique=False, nullable=False)
    correct_answer = db.Column(db.String(70), unique=True, nullable=False)
    incorrect = db.Column(db.String(70), unique=False, nullable=False)
    incorrect2 = db.Column(db.String(70),unique=False, nullable=False)


# Filter by category
@app.route('/quiz/<ct>',methods=["GET"])
def quiz_sc(ct):

    try:
        # Get all question by category

        req = Quiz.query.filter_by(category = "{0}".format(ct)).all()
        num = randint(0,len(req)-1)
        
        res = {
            "id":req[num].id,"category":req[num].category,
            "answers":[
                { "optId":randint(0,100),"opt":req[num].correct_answer },{ "optId":randint(0,100),"opt":req[num].incorrect },
                { "optId":randint(0,100),"opt":req[num].incorrect2 }
            ],"question":req[num].question,"correct":req[num].correct_answer }
            

        return jsonify(res)
    
    except:
        return "ERROR IN GET REQUEST, CATEGORY NOT FOUND"


# Random category
@app.route('/quiz',methods=["GET"])
def quiz_any():
    try:
        # GET all questions

        req = Quiz.query.all()
        num = randint(0,len(req)-1)
        
        res = {
            "id":req[num].id,"category":req[num].category,
            "answers":[
                { "optId":randint(0,100),"opt":req[num].correct_answer },{ "optId":randint(0,100),"opt":req[num].incorrect },
                { "optId":randint(0,100),"opt":req[num].incorrect2 }
            ],"question":req[num].question,"correct":req[num].correct_answer }

        return jsonify(res)
    
    except:
        return "Error in GET REQUEST"
    



if __name__ == '__main__':
    app.run(debug=True,port=5000)