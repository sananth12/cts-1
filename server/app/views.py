import json
import shutil
import os
from config import basedir
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
        obj["qid"] = q.id
        obj["r"] = request.json
        return json.dumps(obj)

    return "did not implement this....?"


@app.route('/validate' , methods = ['POST'])
def validate():
    if request.method == "POST":
        obj = {}
        obj["r"] = request.json
        q = Q_MOD.query.get(int(obj["r"]["qid"]));
        ans = {}
        ans["id"] = obj["r"]["did"]
        if q.answer == obj["r"]["ans"]:
            src = os.path.join(basedir, "private/11111/splits")
            dst = os.path.join(basedir, "app/static")
            src += "/"+str(ans["id"])+".jpg"
            dst += "/"+str(ans["id"])+".jpg"
            shutil.copyfile(src,dst)
            ans["status"] = "success"
            ans["url"] = "/static/"+str(ans["id"])+".jpg"
        else:
            ans["status"] = "failure"

        return json.dumps(ans)
