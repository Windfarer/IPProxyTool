import os
import requests
import time
from proxy import Proxy
from sql.sql_manager import SqlManager
import config

API_URL = os.getenv("API_URL")

sql = SqlManager()

def get_ips():
    resp = requests.get(API_URL)
    if 'ERROR' in resp.text:
        print(resp.text)
        return []
    else:
        return resp.text.split('\n')

def import_ips():
    ips = get_ips()
    for i in ips:
        try:
            ip, port = i.split(":")
        except Exception:
            continue
        proxy = Proxy()
        proxy.set_value(
            ip=ip,
            port=port,
            country="china",
            anonymity=2,
            source="kuaidaili_importer"
        )
        print("kuaidaili_import: {}".format(i))
        sql.insert_proxy(config.free_ipproxy_table, proxy)
    sql.commit()

if __name__ == "__main__":
    if not API_URL:
        print("no API_URL")
        exit()
    while 1:
        try:
            import_ips()
        except Exception as e:
            print(e)
            pass
        print("kuaidaili_sleep 8")
        time.sleep(8)
