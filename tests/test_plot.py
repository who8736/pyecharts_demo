# -*- coding:utf-8 -*-
# author:who8736
# datetime:2020/12/11 21:52

from pcharts.models.plot import bar_base


def test_bar_base(ts_codes):
    bar_base(ts_codes)


if __name__ == '__main__':
    ts_codes = ['000001.SZ', '000002.SZ']
    test_bar_base(ts_codes)
