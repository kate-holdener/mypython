from app import app
from flask import request
from app.tools.sum import sum
from app.tools.product import product

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/add')
def add():
    data = request.args.get('data', None)
    _list = list(map(int, data.split(',')))
    
    total = sum(_list)
    return 'Result= ' + str(total)

@app.route('/multiply')
def multiply():
    data = request.args.get('data', None)
    _list = list(map(int, data.split(',')))
    
    total = product(_list)
    return 'Result= ' + str(total)


