import json
from random import randint
from flask import render_template, flash, redirect, request
from app import app, db
from forms import Questions
from models import Q_MOD

@app.route('/')
@app.route('/index')
def index():
    return render_template("test.html", user={'nick':'test'})

@app.route('/set_ques', methods = ['GET', 'POST'])
def set():
    form = Questions()
    if form.validate_on_submit():
        row = Q_MOD(question=form.question.data, answer=form.answer.data)
        db.session.add(row)
        db.session.commit()
        flash("Your Question was successfully submitted")
        return redirect('/index')
    return render_template('questions.html', form=form)

@app.route('/rules')
def rules():
    return render_template("rules.html")

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/get_q', methods = ['POST'])
def get_q():
    if request.method == "POST":
        q = Q_MOD.query.all()
        l = len(q)
        q = Q_MOD.query.get(randint(1,l))
        obj = {}
        obj["q"] = q.question
        obj["a"] = q.answer
        obj["r"] = request.json
        return json.dumps(obj)

    return "did not implement this....?"
