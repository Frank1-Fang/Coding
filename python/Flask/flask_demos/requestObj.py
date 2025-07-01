from flask import request, Flask

app = Flask(__name__)

# 显示一个简单的表单界面（返回 HTML 字符串）
@app.route('/')
def form():
    return '''
        <h1>请输入你的名字</h1>
        <form method="POST" action="/submit">
            <input type="text" name="username" required>
            <button type="submit">提交</button>
        </form>
    '''

# 处理表单提交并返回问候语
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    if username:
        return f'<h2>Hello, {username}!</h2><a href="/">返回</a>'
    else:
        return '<h2>请输入有效用户名</h2><a href="/">返回</a>'

if __name__ == '__main__':
    app.run(debug=True)
