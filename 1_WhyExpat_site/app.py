from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request
import os

import pandas as pd
import numpy as np
import simplejson as json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

database = {
    'user': '',
    'password': '',
    'port': '3306',
    'host': '127.0.0.1',
    'database': 'projectwe',
    'driver': None
}

if database['driver'] is not None:
    db_prefix += database['driver']

DATABASE_URL = f"mysql+pymysql://{database['user']}:{database['password']}@{database['host']}:{database['port']}/{database['database']}"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL or os.environ.get(
    'DATABASE_URL', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class why_expat_table(db.Model):
    __tablename__ = "why_expat_table"

    test_id = db.Column(db.Integer, primary_key=True)
    satisfaction_level = db.Column(db.VARCHAR(20))
    last_evaluation = db.Column(db.VARCHAR(20))
    number_project = db.Column(db.VARCHAR(20))
    average_montly_hours = db.Column(db.VARCHAR(20))
    work_accident = db.Column(db.VARCHAR(20))
    promotion_last_5years = db.Column(db.VARCHAR(20))
    salary = db.Column(db.VARCHAR(20))
    leader_host = db.Column(db.VARCHAR(20))
    culture_home = db.Column(db.VARCHAR(20))
    culture_host = db.Column(db.VARCHAR(20))
    function_host = db.Column(db.VARCHAR(20))
    business_size_host = db.Column(db.VARCHAR(20))
    economic_perspective_host = db.Column(db.VARCHAR(20))


@app.route("/")
def index():
    """Homepage"""
    return render_template("index.html")


@app.route("/who-we-are")
def whoweare():
    """Who We Are"""
    return render_template("who-we-are.html")


@app.route("/background")
def background():
    """Background"""
    return render_template("background.html")


@app.route("/our-goals")
def ourgoals():
    """Our Goals"""
    return render_template("our-goals.html")


@app.route("/our-tools")
def ourtools():
    """Our Tools"""
    return render_template("our-tools.html")


@app.route("/questionnaire", methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'GET':
        return render_template("questionnaire.html")

    we_summary = why_expat_table(satisfaction_level=request.form['satisfaction_level'],
                                 last_evaluation=request.form['last_evaluation'], number_project=request.form['number_project'], average_montly_hours=request.form['average_montly_hours'], work_accident=request.form['work_accident'], promotion_last_5years=request.form['promotion_last_5years'], salary=request.form['salary'], leader_host=request.form['leader_host'], culture_home=request.form['culture_home'], culture_host=request.form['culture_host'], function_host=request.form['function_host'], business_size_host=request.form['business_size_host'], economic_perspective_host=request.form['economic_perspective_host'])

    db.session.add(we_summary)
    db.session.commit()
    return render_template('questionnaire.html')


if __name__ == "__main__":
    app.run()
