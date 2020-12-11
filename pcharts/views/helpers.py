from flask import Blueprint, render_template, request
from ..models.sqlhelper import readStocks

helpers = Blueprint('helpers', __name__)


@helpers.route("/stocks")
def readstocks():
    stocks = readStocks()
    # stocks = stocks[:10]
    # stocks.rename(columns={'ts_code': 'id'}, inplace=True)
    stocks['text'] = stocks.id + ' ' + stocks.name
    # print(stocks.to_json(orient='records', force_ascii=False))
    return stocks.to_json(orient='records', force_ascii=False)
