from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# 初始化数据库
def init_db():
    if not os.path.exists('tasks.db'):
        conn = sqlite3.connect('tasks.db')
        conn.execute('''
            CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                done INTEGER DEFAULT 0
            );
        ''')
        conn.commit()
        conn.close()

def get_db():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
        conn.commit()
        return redirect('/')
    tasks = conn.execute('SELECT * FROM tasks ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    conn = get_db()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        conn.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?', (title, description, task_id))
        conn.commit()
        return redirect('/')
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    conn = get_db()
    task = conn.execute('SELECT done FROM tasks WHERE id = ?', (task_id,)).fetchone()
    new_status = 0 if task['done'] else 1
    conn.execute('UPDATE tasks SET done = ? WHERE id = ?', (new_status, task_id))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
