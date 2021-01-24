# -*- coding: utf-8 -*-
"""
Created on 2016年12月14日

@author: who8736
"""
from pcharts import app
from pcharts.initlog import initlog


if __name__ == '__main__':
    initlog()
    app.run(host='0.0.0.0', port='5001', threaded=True, debug=True)
