import logging
import json
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
    ts_codes = None
    args = request.args.get('ts_codes')
    if args is not None:
        ts_codes = json.loads(args)
    # print(request.args)
    logging.debug(f'ts_codes: {ts_codes}')
    c = bar_base(ts_codes)
    return c.dump_options_with_quotes()


@profits.route("/inc")
def profitsinc():
    # c = bar_base1()
    # return Markup(c.render_embed())
    return render_template("profits/inc.html")
