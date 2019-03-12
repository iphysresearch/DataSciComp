from flask import Flask, render_template, redirect, Response
from flask_frozen import Freezer

import os, sys, yaml, pytz, time, datetime, heapq  # 堆队列
import numpy as np
import click

add_datas = [
    "./_data/_effective_kaggle.yaml",
    "./_data/_effective_drivendata.yaml",
    "./_data/_effective_codalab.yaml",
    "./_data/_effective_challengedata.yaml",
    "./_data/_effective_crowdai.yaml",
    "./_data/_effective_signate.yaml",
    "./_data/_effective_unearthed.yaml",
    "./_data/_effective_analyticsvidhya.yaml",
    "./_data/_effective_GECCO.yaml",
    "./_data/_effective_grand_challenge.yaml",
    "./_data/_effective_herox.yaml",
    "./_data/_effective_ICDAR.yaml",
    "./_data/_effective_kelvins.yaml",
    "./_data/_effective_天池.yaml",
    "./_data/_effective_FUTURELAB_AI.yaml",
    "./_data/_effective_点石.yaml",
    "./_data/_effective_kesci.yaml",
    "./_data/_effective_dcjingsai.yaml",
    "./_data/_effective_datafountain.yaml",
    "./_data/_effective_ICME.yaml",
    "./_data/_effective_EvalAI.yaml",
    "./_data/_effective_others.yaml",
]

competitions = []
for add_data in add_datas:
    with open(add_data, "r", encoding="utf-8") as f:
        cfg = f.read()
        competitions.extend(yaml.load(cfg))
competitions = [
    c
    for c in competitions
    if c["deadtime"] > datetime.date.today().strftime("%Y-%m-%d")
]
competitions.sort(key=lambda x: x["deadtime"])


app = Flask(__name__)


app.config["FREEZER_DESTINATION"] = "docs"
# https://stackoverflow.com/questions/11577147/how-to-fix-page-404-on-github-page
app.config["FREEZER_DESTINATION_IGNORE"] = [".git*", "CNAME", "favicon.ico"]

freezer = Freezer(app)

id_type_checkboxs = [
    {"id": "PF-checkbox", "name": "Platform"}
    # ,{'id': 'IT-checkbox', 'name': 'Industry'}
    ,
    {"id": "AC-checkbox", "name": "Academia"},
]

id_type2_checkboxs = [
    {"id": "DM-checkbox", "name": "Data Mining"},
    {"id": "CV-checkbox", "name": "Computer Vision"},
    {"id": "NLP-checkbox", "name": "Natural Language Processing"},
    {"id": "RL-checkbox", "name": "Reinforcement Learning/Robotics"},
    {"id": "SP-checkbox", "name": "Speech/Signal Proccessing"},
]


@app.route("/")
def index(
    id_type_checkboxs=id_type_checkboxs,
    id_type2_checkboxs=id_type2_checkboxs,
    competitions=competitions,
):
    # 保证每个 comp 的 type 键的值是 list 类型
    [
        comp.update({"type1": [comp["type1"]]})
        for comp in competitions
        if not isinstance(comp["type1"], list)
    ]
    [
        comp.update({"type2": [comp["type2"]]})
        for comp in competitions
        if not isinstance(comp["type2"], list)
    ]
    # 判断 prize
    for comp in competitions:
        if (comp["prize"] == "NaN") or (comp["prize"] == "Kaggle Swag"):
            comp.update({"howprize": ["unrewarded"]})
        else:
            comp.update({"howprize": ["rewarded"]})
    # [ comp.update({'howprize': ['unrewarded']}) for comp in competitions if comp['prize'] == 'NaN']
    # [ comp.update({'howprize': ['rewarded']}) for comp in competitions if comp['prize'] ~= 'NaN']
    return render_template(
        "index.html",
        id_type_checkboxs=id_type_checkboxs,
        id_type2_checkboxs=id_type2_checkboxs,
        competitions=competitions,
    )


with open("./_data/_hosts.yaml", "r", encoding="utf-8") as f:
    cfg = f.read()
    hosts = yaml.load(cfg)


@app.route("/hostby.html")
def hostby(id_type_checkboxs=id_type_checkboxs, hosts=hosts):
    return render_template(
        "hostby.html", id_type_checkboxs=id_type_checkboxs, hosts=hosts
    )


# @app.route('/rss.xml')
# def log(competitions = competitions):
#     num_largest = 2
#     comps_pubtime = np.array([ int(i['pubtime'].replace('-', '')) for i in competitions ])
#     index_largest = [ np.where(comps_pubtime == largest_value)[0].tolist() for largest_value in heapq.nlargest(num_largest, np.unique(comps_pubtime)) ]
#     competitions = [ (competitions[largest_index], block_time) for block_time, largest_time in enumerate(index_largest) for largest_index in largest_time]

#     [ comp.update({'pubtime': datetime.datetime.fromtimestamp(int(datetime.datetime.strptime(comp['pubtime'], '%Y-%m-%d').timestamp()), pytz.timezone('Asia/Shanghai')).strftime("%a, %d %b %Y") }) for comp, _ in competitions ]

#     return render_template('rss.xml', competitions=competitions)


@app.route("/update_log.xml")
def products_xml(competitions=competitions):
    num_largest = 2
    comps_pubtime = np.array([int(i["pubtime"].replace("-", "")) for i in competitions])
    time_largest = heapq.nlargest(num_largest, np.unique(comps_pubtime))
    index_largest = [
        np.where(comps_pubtime == largest_value)[0].tolist()
        for largest_value in time_largest
    ]
    competitions = [
        (competitions[largest_index], block_time)
        for block_time, largest_time in enumerate(index_largest)
        for largest_index in largest_time
    ]

    [
        comp.update(
            {
                "pubtime": datetime.datetime.fromtimestamp(
                    int(
                        datetime.datetime.strptime(
                            comp["pubtime"], "%Y-%m-%d"
                        ).timestamp()
                    ),
                    pytz.timezone("Asia/Shanghai"),
                ).strftime("%a, %d %b %Y")
            }
        )
        for comp, _ in competitions
    ]

    output = '<?xml version="1.0" encoding="UTF-8" ?>'
    output += '<rss version="2.0">'
    output += "<channel>"
    output += "<title>Data Science Challenge / Competition</title>"
    output += "<link>https://iphysresearch.github.io/DataSciComp</link>"

    update_block = [
        datetime.datetime.fromtimestamp(
            int(
                datetime.datetime.strptime(
                    str(time_largest[block]), "%Y%m%d"
                ).timestamp()
            ),
            pytz.timezone("Asia/Shanghai"),
        ).strftime("%m/%d/%Y")
        for block in range(num_largest)
    ]
    output += "<description>Latest update at {} (GMT+0800).</description>".format(
        update_block[0]
    )

    for comp, _ in competitions:
        output += "<item>"
        output += "<title>{:s}</title>".format(comp["title"])
        output += "<link>{:s}</link>".format(comp["url"])
        output += "<category>{:s}</category>".format("/".join(comp["type1"]))
        output += "<category>{:s}</category>".format("/".join(comp["type2"]))
        output += "<pubDate>{:s}</pubDate>".format(comp["pubtime"])
        output += "<description>{:s}</description>".format(
            comp["note"].replace("<br>", "")
        )
        output += "</item>"
    output += "</channel>"
    output += "</rss>"
    return Response(output, mimetype="application/xml")


if __name__ == "__main__":
    # freezer.freeze()
    freezer.run(debug=True)
