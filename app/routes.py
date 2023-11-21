from flask import render_template, request, redirect, url_for
from app import app
import sqlite3


@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            comment TEXT
        )
    ''')
    data = conn.execute('SELECT * FROM user_data').fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    username = request.form['username']
    comment = request.form['comment']

    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO user_data (username, comment) VALUES (?, ?)', (username, comment))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))