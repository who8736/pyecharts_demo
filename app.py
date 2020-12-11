from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from jinja2 import Environment, FileSystemLoader
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import CurrentConfig
import pandas as pd

from sqlconn import engine

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

app = Flask(__name__)
# app = Flask(__name__, static_folder="templates")
app.debug = True
app.secret_key = '34u3uoifopxf3'
CSRFProtect(app)
Bootstrap(app)


def bar_base() -> Bar:
    c = Bar()
    c.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    c.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    c.add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    return c


@app.route("/")
def index():
    # c = bar_base1()
    # return Markup(c.render_embed())
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    readProfits()
    return c.dump_options_with_quotes()


def readProfits():
    ts_code = '000002.SZ'
    sql = f'select ttmprofits from ttmprofits where ts_code="{ts_code}"'
    df = pd.read_sql(sql, engine)
    print(df)

if __name__ == "__main__":
    app.run(debug=True)
