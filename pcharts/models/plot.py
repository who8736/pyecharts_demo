from pyecharts import options as opts
from pyecharts.charts import Bar
from .sqlhelper import readProfits


def bar_base() -> Bar:
    df = readProfits()
    print(df)
    c = Bar()
    c.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    c.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    c.add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    return c