import sqlite3

# sqlite3是一个微型的数据库，主要用于浏览器、手机/平板、手机和智能设备
# 支持标准的sql语句，不过没有特定的数据类型，可以根据开发语法的特性或类型，来限定字段的类型
conn = sqlite3.connect('users.db')  # 如果文件不存你在会自动创建

cursor = conn.cursor()
cursor.execute('''
   CREATE TABLE user(id Integer PRIMARY KEY,name,age,phone)
''')

cursor.execute('''
INSERT INTO user(name,age,phone) 
values ('disen',20,'17791692095')
''')

cursor.execute('SELECT * FROM user')

for row in cursor.fetchall():
    print(row)
