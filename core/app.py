
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
1
2
3
4
5
6
7
from bottle import route, run, template
 
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
 
run(host='localhost', port=8080)
