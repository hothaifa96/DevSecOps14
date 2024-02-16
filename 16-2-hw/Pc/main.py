from flask import Flask
import requests


app = Flask(__name__)

pc_list=[
    {'brand':'hp','cpu':16,'color':'red'},
    {'brand':'lenovo','cpu':16,'color':'yellow'}
]

@app.get('/')
def main_page():
    return "hello",200

@app.get('/pc')
def get_all():
    return pc_list

@app.get('/pc/<int:id>')
def get_by_id(id):
    return pc_list[id-1]





app.run(port=5000,host='0.0.0.0')