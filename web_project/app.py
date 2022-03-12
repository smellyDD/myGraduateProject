# -*- coding = utf-8 -*-
# @Time : 2021/12/7 17:12
# @File : app.py
# @Software : PyCharm
import datetime
from flask import Flask
from flask import render_template
from web_project.Source import Demo

app = Flask(__name__)
app.jinja_env.variable_start_string = '{{ '
app.jinja_env.variable_end_string = ' }}'


@app.route('/')
def index():
    data_form = Demo(date='2022-03-01')
    return render_template("index_novue.html", form=data_form)


if __name__ == '__main__':
    app.run(debug=True)
