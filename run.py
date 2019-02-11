from flask import Flask, render_template, redirect
from flask_frozen import Freezer

import os, sys, yaml
import click

add_datas = ['./_data/_effective_kaggle.yaml',
            './_data/_effective_drivendata.yaml',
            './_data/_effective_codalab.yaml',
            './_data/_effective_challengedata.yaml',
            './_data/_effective_crowdai.yaml',
            './_data/_effective_signate.yaml',
            './_data/_effective_unearthed.yaml',
            './_data/_effective_analyticsvidhya.yaml',
            './_data/_effective_GECCO.yaml',
            './_data/_effective_grand_challenge.yaml',
            './_data/_effective_kelvins.yaml',
            './_data/_effective_天池.yaml',
            './_data/_effective_点石.yaml',
            './_data/_effective_kesci.yaml',
            './_data/_effective_dcjingsai.yaml',
            './_data/_effective_datafountain.yaml',
            './_data/_effective_ICME.yaml',
            './_data/_effective_others.yaml']

competitions = []
for add_data in add_datas:
    with open(add_data, 'r', encoding='utf-8') as f:
        cfg = f.read()
        competitions.extend(yaml.load(cfg))
competitions.sort(key=lambda x: x['deadtime'])


app = Flask(__name__)


app.config['FREEZER_DESTINATION'] = 'docs'
# https://stackoverflow.com/questions/11577147/how-to-fix-page-404-on-github-page
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME','favicon.ico']

freezer = Freezer(app)

id_type_checkboxs = [
    {'id': 'PF-checkbox', 'name': 'Platform'}
    # ,{'id': 'IT-checkbox', 'name': 'Industry'}
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


with open('./_data/_hosts.yaml', 'r', encoding='utf-8') as f:
    cfg = f.read()
    hosts = yaml.load(cfg)

@app.route('/hostby.html')
def hostby(id_type_checkboxs = id_type_checkboxs, hosts = hosts):

    return render_template('hostby.html', id_type_checkboxs=id_type_checkboxs, hosts = hosts)


if __name__ == '__main__':
    # freezer.freeze()
    freezer.run(debug=True)