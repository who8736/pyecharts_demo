from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar

app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
            .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


def bar_base1() -> Bar:
    c = Bar()
    c.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    c.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    c.add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    return c


@app.route("/")
def index():
    c = bar_base1()
    return Markup(c.render_embed())


if __name__ == "__main__":
    app.run(debug=True)
