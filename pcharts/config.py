import os

# 用于flask CSRF 的配置
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
sqlUser = 'root'
sqlPassword = ''
sqlIp = '127.0.0.1'

if os.path.isfile('config_priv.py'):
    from config_priv import *
