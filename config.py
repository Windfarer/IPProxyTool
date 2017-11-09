# coding=utf-8

DB_config = {
    # 'db_type': 'mongodb',
    'db_type': 'mysql',

    'mysql': {
        'host': '192.168.5.103',
        'port': 3306,
        'user': 'root',
        'password': 'password',
        'charset': 'utf8',
    }
}

database = 'ipproxy'
free_ipproxy_table = 'free_ipproxy'
httpbin_table = 'httpbin'

data_port = 8000
