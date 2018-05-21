from app import app
from flask import request
from flask import redirect
from flask import jsonify
from flask import json

@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
        return json.dumps(dict1["data"])
    else:
        return '<h1>只接受post请求！</h1>'

@app.route('/user/<name>')
def user(name):
    return'<h1>hello, %s</h1>' % name

@app.route('/blog/<id>', methods=['GET', 'POST'])
def blog(id):
    if request.method == 'POST':
        data = {'title':'炮打司令部','context':'我的第一篇大字报','time':'2018/05/21'}
        return json.dumps(data)
    else:
        return '<h1>只接受post请求！</h1>'

if __name__ =='__main__':
    app.run(debug=True)