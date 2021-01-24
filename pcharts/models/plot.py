from pyecharts import options as opts
from pyecharts.charts import Bar
from .sqlhelper import readProfits, readStockName


def bar_base(ts_codes) -> Bar:
    assert ts_codes is not None, '股票代码为空'
    # if ts_codes is None:
    #     ts_codes = ['000001.SZ']
    df = readProfits(ts_codes)
    print(df)
    c = Bar()
    stocks = []
    for key, data in df.iteritems():
        if key == 'end_date':
            c.add_xaxis(data.to_list())
        else:
            name = readStockName(key)
            title = f'{key} {name}'
            stocks.append(title)
            c.add_yaxis(title, data.to_list())
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-基本示例",
                                  subtitle=', '.join(stocks)))
    return c
