import pandas as pd


def readProfits():
    ts_code = '000002.SZ'
    sql = f'select ttmprofits from ttmprofits where ts_code="{ts_code}"'
    df = pd.read_sql(sql, engine)
    print(df)