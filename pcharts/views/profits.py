import logging
from flask import Blueprint, render_template, request

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
    ts_code = request.args.get('ts_code')
    logging.debug(f'ts_code: {ts_code}')
    c = bar_base()
    return c.dump_options_with_quotes()


@profits.route("/inc")
def profitsinc():
    # c = bar_base1()
    # return Markup(c.render_embed())
    return render_template("profits/inc.html")
