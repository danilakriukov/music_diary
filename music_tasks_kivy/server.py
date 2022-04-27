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
  conn = sqlite3.connect('tasks.db')
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS tasks (tasks);")
  cursor.execute("DELETE FROM tasks ")
  cursor.execute ("INSERT INTO tasks VALUES ('play piano')")
  cursor.execute("SELECT * FROM tasks")
  conn.commit()
  return 'works!'


if __name__ == "__main__":
 app.run()