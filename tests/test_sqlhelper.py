# -*- coding:utf-8 -*-
# author:who8736
# datetime:2020/12/11 21:44

from pcharts.models.sqlhelper import readProfits, readStockName


def test_readStockName(ts_code):
    name = readStockName(ts_code)
    print(name)


def test_readProfits(ts_codes):
    result = readProfits(ts_codes)
    print(result)


if __name__ == '__main__':
    # ts_code = '000025.SZ'
    # test_readStockName(ts_code)

    ts_codes = ['000001.SZ', '000002.SZ']
    test_readProfits(ts_codes)
