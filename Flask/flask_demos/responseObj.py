from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/custom_response') # http://127.0.0.1:5000/custom_response
def custom_response():
    user_agent = request.headers.get('User-Agent', 'Unknown')

    # 创建响应体
    body = f"""
        <h1>This is a custom response!</h1>
        <p>Your browser is: {user_agent}</p>
    """

    # 构造响应对象
    response = make_response(body, 200)  # 第二个参数是状态码 200 OK

    # 添加自定义响应头
    response.headers['X-Custom-Header'] = 'HelloFromFlask'
    response.headers['Content-Type'] = 'text/html; charset=utf-8'

    return response

if __name__ == '__main__':
    app.run(debug=True)
