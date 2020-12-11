from flask import Flask, render_template, Blueprint
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
from pcharts.models.plot import bar_base

# CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

profits = Blueprint('profits', __name__)


@profits.route("/")
def index():
    # c = bar_base1()
    # return Markup(c.render_embed())
    return render_template("profits/index.html")


@profits.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


@profits.route("/inc")
def profitsinc():
    # c = bar_base1()
    # return Markup(c.render_embed())
    return render_template("profits/inc.html")

