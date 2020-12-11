import pandas as pd
from .sqlconn import engine


def readProfits():
    ts_code = '000002.SZ'
    sql = f'select ttmprofits from ttmprofits where ts_code="{ts_code}"'
    df = pd.read_sql(sql, engine)
    print(df)

def readStocks():
    """读取股票清单"""
    sql = 'select ts_code id, name from stock_basic'
    df = pd.read_sql(sql, engine)
    return df
