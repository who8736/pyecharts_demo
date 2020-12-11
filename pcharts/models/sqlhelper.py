import pandas as pd
from .sqlconn import engine


def readProfits(ts_codes, startDate=None, endDate=None):
    if ts_codes is None:
        ts_codes = ['000002.SZ']
    if startDate is None:
        startDate = '20190101'
    if endDate is None:
        endDate = '20201231'

    result = None
    for ts_code in ts_codes:
        sql = f'''select end_date, ttmprofits `{ts_code}` from ttmprofits 
                    where ts_code="{ts_code}" 
                        and end_date>="{startDate}"
                        and end_date<="{endDate}"'''
        df = pd.read_sql(sql, engine)
        df[ts_code] = df[ts_code] / 10000 / 10000
        df[ts_code] = df[ts_code].round(2)
        # print(df)
        if result is None:
            result = df.copy()
        else:
            result = result.merge(df, on='end_date', how='outer')
    result['end_date'] = result['end_date'].apply(lambda x: x.strftime('%Y%m%d'))
    return result


def readStockName(ts_code):
    sql = f'select name from stock_basic where ts_code="{ts_code}"'
    df = pd.read_sql(sql, engine)
    if not df.empty:
        return df.iloc[0, 0]


def readStocks():
    """读取股票清单"""
    sql = 'select ts_code id, name from stock_basic'
    df = pd.read_sql(sql, engine)
    return df
