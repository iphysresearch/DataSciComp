<h1>Important Terminology!</h1>
<p>
This Repo was permanently <b>archived</b> in 2019/10/01. <b>BUT this is not the end！</b><br>
  </p>
  <p>
With almost 3 months together in joint development, the project has been reborn once more! <br>
We convert our website from static to dynamic such that everyone can submit a challenge/competition on their own interests. And more functions are coming. Please look forward to it!
</p>
<p>
Click <a href="https://www.datascicamp.com">HERE</a> for our new website! You can also move to <a href="https://github.com/datascicamp/DataSciCamp">Welcome page</a> for more infomations.
</p>

---
---
- The archived README text below
- 以下是存档的 README 原文本
---
---

<div align="center">
  <a href="./favicon.ico">
    <img width="30" heigth="30" src="./favicon.ico">
  </a>
  <br>
  <br>
    <h1>Data Science Challenges / Competition Deadlines </h1>
  <p>
      <li>A collection of popular Data Science Challenges/Competitions</li>
      <li>Countdown timers to keep track of the entry deadlines.</li>
    <br><a href="https://www.datascicamp.com">DataSciCamp.com</a>
  <p>
</div>


> Please *Feel free to star* ⭐ this repo! or open an issue with your suggestions and requests!
>
> 欢迎关注微博更新：[IPhysResearch](http://weibo.com/IPhysresearch) . Collected by 土豆 (Herb) in spare time.
>
> 联系网站开发者：[LeonTian 的知乎主页](https://www.zhihu.com/people/winchester-26/activities) . LeonTian (Chief Designer and Developer of DataSciCamp).

---

> ###### [Description](#description) | [How to Contribute](#how-to-Contribute) | [Data Format](#data-format) | [To-Do](#to-do) | [Feature Requests](#feature-requests) | [FAQ](#faq) | [Acknowledgments & other useful listings](#acknowledgments-and-other-useful-listings) | [Stargazers over time](#stargazers-over-time) | [License](#license)

---

## Description

- First-Class tags: `Platform`  / `Academia`

  - `Platform`: Online public communities and platforms containing various challenges/competitions.
  - `Academia`: Challenges/competitions for academic research.

- Second-Class tags: `Data Mining` / `Computer Vision` / `Natural Language Processing` / `Reinforcement Learning/Robotics` / `Speech/Signal Proccessing`

  - Note: `Data Mining` for structured data sources, the others for unstructured ones.

- `Rewards filter` tags show you the challenges/competitions offered prizes. 
- The Countdowns to **ENTRY DEADLINE** with respect to visitor's local time with time zone support.
- `Prize` for total prize.



## How to Contribute

- Please **post issues** if you find difficulty or inconvenience with any of them, or if any of them are no longer in operation, or if you encounter bugs or issues on the website.

- To add/update a challenge or any feedbacks to me, please don't hesitate and send in a **pull request**.

  - The easiest way to do that is to directly append the details of challenges/competitions in `./_data/_*.yaml` with **YAML** format. (see [Data Format](#data-format) and  `./_data/readme`)

  - Or you can clone the repo and **push** your changes up. Here's how you can build it by your own:

    ```bash
    $ pipenv install --dev
    $ export FLASK_APP=run.py
    $ python run.py
    ```

- A WeChat group have been created: <a target='_blank' href="https://i.loli.net/2019/07/23/5d372ba49502080881.png">QR code</a> (7月30日前有效)





## Data Formats Available

The entire dataset is stored in files `./_data/_effective_*.yaml` and `./_data/_hosts.yaml`.

Here is an example:

```yaml
- id: TrackML_Throughput_Phase
  type1: 
    - PF
    - AC
  type2:
    - DM
    - CV
  title: TrackML Throughput Phase
  url: https://competitions.codalab.org/competitions/20574
  hostby:
    - CodaLab: https://competitions.codalab.org
    - NeurIPS 2018: https://nips.cc/Conferences/2018/CompetitionTrack
  range: Sept. 7, 2018 - March 12, 2019
  deadtime: "2019-03-12 23:59:59"
  timezone: UTC
  pubtime: '2019-02-15'
  note: 'The overall TrackML challenge web site is <a href="https://sites.google.com/site/trackmlparticle/">there</a>.'
  prize: $15,000
```

See more details: `./_data/readme`


## To-Do

- [ ] 双语化？
- [x] Add subscription / notification?
- [ ] Add past challenges/competitions?（增加历史赛题集锦？）
- [ ] Upgrade to a dynamic site. （升级成动态站点）
- [ ] A more handy way to add/update by any visitors.（更方便的表单填写实现赛题增加/更新）
- [ ] Auto-update infos by crawling target site.（定时爬虫监控目标站点的赛题信息更新）


## Feature Requests

Help us imporve DataSciComp!

如果你还想 DataSciComp 支持新的特性和功能，请使用 [FeatHub](https://feathub.com/iphysresearch/DataSciComp) 进行投票，我们将综合考虑投票结果等因素来确定开发的优先级。

[![Feature Requests](https://cloud.githubusercontent.com/assets/390379/10127973/045b3a96-6560-11e5-9b20-31a2032956b2.png)](http://feathub.com/iphysresearch/DataSciComp)

[![Feature Requests](http://feathub.com/iphysresearch/DataSciComp?format=svg)](http://feathub.com/iphysresearch/DataSciComp)


## FAQ

- Where is the last `markdown` version?
  - see [README_old.md](https://github.com/iphysresearch/DataSciComp/blob/master/README_old.md)
- 第一次打开站点发现所有赛题显示不正常，看到满眼 `Entry Deadline:` 的话，请科学上网后再试一次:joy: ​。
- 如果还有某种页面显示不正常的问题，请清空 cookies 和缓存再试一次:sob: 。



## Acknowledgments and other useful listings

- [Flask](http://flask.pocoo.org) - *a microframework for Python based on Werkzeug, Jinja 2 and good intentions.*
- Thanks to Abhishek Das for building the original site, [ai-deadlin.es](http://aideadlin.es)!
- Thanks to [W3school](http://www.w3school.com.cn), [CODEPLY](https://www.codeply.com) and [Bootstrap](https://bootstrapdocs.com/v3.3.6/docs/css/) for HTML/CSS/JScript which helped me *my first* design experience.
- [geodeadlin.es](http://geodeadlin.es/) by @LukasMosser
- [neuro-deadlines](https://github.com/tbryn/neuro-deadlines) by @tbryn
- [ai-challenge-deadlines](https://github.com/dieg0as/ai-challenge-deadlines) by @dieg0as
- [2018-2019 International Conferences in AI, CV, DM, NLP and Robotics](https://jackietseng.github.io/conference_call_for_paper/2018-2019-conferences-with-ccf.html) by @JackieTseng
- [CV-oriented ai-deadlines (with an emphasis on medical images)](https://creedai.github.io/ai-deadlines/) by @duducheng
- [A searchable compilation of Kaggle past solutions](http://ndres.me/kaggle-past-solutions/) by @[EliotAndres](https://github.com/EliotAndres)
- [Data competition Top Solution 数据竞赛top解决方案开源整理](https://github.com/Smilexuhc/Data-Competition-TopSolution) by @[Smilexuhc](https://github.com/Smilexuhc)
- [Chinese Data Competitions' Solutions | CDCS 中国数据竞赛优胜解集锦](https://github.com/geekinglcq/CDCS) by @[geekinglcq](https://github.com/geekinglcq)
- [ApacheCN 中文开源组织](http://www.apachecn.org) | 专注于优秀项目维护的开源组织 [[Github](https://github.com/apachecn), [Kaggle 项目实战（教程）](https://github.com/apachecn/kaggle)]



## Stargazers over time

[![Stargazers over time](https://starcharts.herokuapp.com/iphysresearch/DataSciComp.svg)](https://starcharts.herokuapp.com/iphyresearch/DataSciComp)



## License

MIT

