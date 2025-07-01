from flask import Flask, request, render_template, redirect
import sqlite3
import os

app = Flask(__name__) # Flask 框架提供的一个类，表示“一个网站应用”

def init_db():
    if not os.path.exists('messages.db'): # 用 sqlite3 库连接 messages.db 数据库；
                                          # 若 messages.db 不存在，则新建一个
        conn = sqlite3.connect('messages.db') # conn 为数据库连接对象，后面执行 SQL 就通过 conn

        # SQL 语句
        conn.execute('''
            CREATE TABLE messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        conn.commit() # 提交到数据库 messages.db
        conn.close() # 关闭数据库连接，释放系统资源

def get_db_connection(): # 需要访问数据库时都可以调用这个函数来获取连接
    conn = sqlite3.connect('messages.db')
    conn.row_factory = sqlite3.Row # 把查询结果的返回格式设置为“字典风格的对象”
                                   # 本来只能用 index 访问 e.g. row[0]
                                   # 现在可以用 列名 访问 e.g. row['username']
    return conn

@app.route('/', methods=['GET', 'POST']) # Flask 路由装饰器
                                         # 当用户访问网站的根路径 / 时，执行下面的 index() 函数
                                         # 允许处理两种 HTTP 方法：GET（读取页面） 和 POST（提交表单）
                                         # 路由 route 决定了哪个 URL 对应哪个函数(这里 '/' 对应了 index() 函数)
def index():
    if request.method == 'POST': # POST 请求：提交留言
        username = request.form['username'] # 从用户提交的表单中提取输入框 name="username" 的内容
        content = request.form['content']
        if username.strip() and content.strip(): # strip() 去除首尾空格，都非空才写入数据库
            conn = get_db_connection() # 打开 SQLite 数据库连接
            conn.execute('INSERT INTO messages (username, content) VALUES (?, ?)', (username, content)) # execute 执行插入语句
            conn.commit()
            conn.close()
        return redirect('/') # 重定向到主页，防止用户刷新时重复提交表单
    else:
        conn = get_db_connection() # GET 请求： 打开网页或提交后跳转回来
        messages = conn.execute('SELECT * FROM messages ORDER BY created_at DESC').fetchall()
        conn.close()
        return render_template('index.html', messages=messages) # 渲染 templates/index.html 页面，并把 messages 数据传过去

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
