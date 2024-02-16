import time

from flask import Flask, request
import requests

app = Flask(__name__)

pc_list = [
    {'brand': 'hp', 'cpu': 16, 'color': 'red'},
    {'brand': 'lenovo', 'cpu': 16, 'color': 'yellow'}
]


@app.get('/')
def main_page():
    return "hello", 200


@app.get('/pc')
def get_all():
    return pc_list


@app.get('/pc/<int:id>')
def get_by_id(id):
    return pc_list[id - 1]


@app.post('/pc')
def add_pc():
    new_data = request.json
    keys = list(pc_list[0].keys())
    for key in keys:  # validation
        if key not in new_data.keys():
            return f"missing {key} ", 400
    pc_list.append(new_data)
    return {'Status': "Done", 'message': 'new pc added'}


@app.put('/pc/<int:id>')
def update_pc(id):
    new_data = request.json
    pc_list.pop(id - 1)
    pc_list.insert(id - 1, new_data)
    return {'Status': "Done", 'message': 'pc updated'}


@app.delete('/pc/<int:id>')  # multi path functions
def delete_pc(id):
    pc_list.pop(id - 1)
    return {'Status': "Done", 'message': 'pc deleted'}



@app.get('/test')
def is_healthy():
    return "200",200


@app.get('/healthy')
def is_ready():
    time.sleep(10)
    res = requests.get('https://www.google.com')
    if res.status_code <400:
        return "200",200
    return '400',400


# @app.after_request()
# def after():
# @app.before_request()
# def after():


app.run(port=5000, host='0.0.0.0')
