import mysql.connector

# MySQL数据库连接信息
mysql_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'justforme999',
    'database': 'server_demo'
}

# 创建数据库连接
db_connection = mysql.connector.connect(**mysql_config)

# 创建游标对象
db_cursor = db_connection.cursor()

# 执行查询
db_cursor.execute("SELECT * FROM my_table")

# 获取查询结果
result = db_cursor.fetchall()

# 打印结果
for row in result:
    print(row)

# 关闭游标和连接
db_cursor.close()
db_connection.close()
