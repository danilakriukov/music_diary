from flask import Flask, render_template, request, redirect, url_for, jsonify
import time
from datetime import datetime
import pickle
import sqlite3


app = Flask(__name__)


@app.route('/')
def begin():
 return redirect(url_for('main'))


@app.route('/main')
def main():
  conn = sqlite3.connect('frenchdb.db')
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS frenchdb (frenchdb);")
  cursor.execute("DELETE FROM frenchdb ")
  cursor.execute ("INSERT INTO frenchdb VALUES ('souvent')")
  cursor.execute("SELECT * FROM frenchdb")
  conn.commit()
  frenchdb = cursor.fetchall()
  return render_template("main.html",frenchdb=frenchdb)


@app.route('/updated', methods=['POST'])
def update():
 conn = sqlite3.connect('frenchdb.db')
 cursor = conn.cursor()
 cursor.execute ("INSERT INTO frenchdb VALUES ('arbre')")
 conn.commit()
 cursor.execute("SELECT * FROM frenchdb")
 word = cursor.fetchall()
 #myitem = random.choice(mylist)
 return jsonify('',render_template('model.html',frenchdb=word))


@app.route('/dataprocess', methods=['POST'])
def dataprocess():
    word = request.form.get("wordinput")
    print(word)           
    return jsonify('',render_template('model.html',frenchdb=word))


if __name__ == "__main__":
 app.run()