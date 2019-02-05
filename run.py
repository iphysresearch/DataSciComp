from flask import Flask, render_template, redirect
from flask_frozen import Freezer

import os, sys, yaml
import click

with open('./_data/_effective.yaml', 'r', encoding='utf-8') as f:
    cfg = f.read()
    competitions = yaml.load(cfg)

app = Flask(__name__)
freezer = Freezer(app)

id_name_checkboxs = [
    {'id': 'PF-checkbox', 'name': 'Platform'}
    ,{'id': 'IT-checkbox', 'name': 'Industry'}
    ,{'id': 'AC-checkbox', 'name': 'Academia'} 
]

@app.route('/')
@app.route('/greet/<name>')
def index(id_name_checkboxs = id_name_checkboxs, competitions = competitions):
    # 保证每个 comp 的 type 键的值是 list 类型
    [ comp.update({'type': [comp['type']]}) for comp in competitions if not isinstance(comp['type'], list) ]
    return render_template('index.html', id_name_checkboxs=id_name_checkboxs, competitions=competitions)

if __name__ == '__main__':
    # freezer.freeze()
    freezer.run(debug=False)