from flask import Flask, render_template, redirect
from flask_frozen import Freezer

import os, sys, yaml
import click

with open('./_data/_effective.yaml', 'r', encoding='utf-8') as f:
    cfg = f.read()
    competitions = yaml.load(cfg)
    competitions.sort(key=lambda x: x['deadtime'])

app = Flask(__name__)
freezer = Freezer(app)

id_type_checkboxs = [
    {'id': 'PF-checkbox', 'name': 'Platform'}
    ,{'id': 'IT-checkbox', 'name': 'Industry'}
    ,{'id': 'AC-checkbox', 'name': 'Academia'} 
]

id_type2_checkboxs = [
    {'id': 'DM-checkbox', 'name': 'Data Mining'}
    ,{'id': 'CV-checkbox', 'name': 'Computer Vision'}
    ,{'id': 'NLP-checkbox', 'name': 'Natural Language Processing'} 
    ,{'id': 'RL-checkbox', 'name': 'Reinforcement Learning/Robotics'} 
    ,{'id': 'SP-checkbox', 'name': 'Speech/Signal Proccessing'} 
]

@app.route('/')
def index(id_type_checkboxs = id_type_checkboxs, id_type2_checkboxs = id_type2_checkboxs, competitions = competitions):
    # 保证每个 comp 的 type 键的值是 list 类型
    [ comp.update({'type1': [comp['type1']]}) for comp in competitions if not isinstance(comp['type1'], list) ]
    [ comp.update({'type2': [comp['type2']]}) for comp in competitions if not isinstance(comp['type2'], list) ]
    return render_template('index.html', id_type_checkboxs=id_type_checkboxs, 
                                         id_type2_checkboxs=id_type2_checkboxs,
                                         competitions=competitions)

if __name__ == '__main__':
    # freezer.freeze()
    freezer.run(debug=False)