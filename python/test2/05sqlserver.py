# encoding=utf-8

import pymssql

# 创建数据库连接
def createConnection():
    conn = pymssql.connect(server='192.168.1.65', user='sa', password='Wheatek!', database='OTA')
    return conn

#关闭数据库连接。
def closeConnection(conn):
    conn.close()

#插入一行数据
def insertRow(conn):
    print("开始插入数据")
    cursor = conn.cursor()
    #cursor.execute("insert into Product([Name], ProductNumber) values('SQL Server Express', 'SQLEXPRESS');")
    cursor.execute("insert into Product([Name], ProductNumber) OUTPUT INSERTED.ProductId values('SQL Server Express', 'SQLEXPRESS');")
    #如果在这里调用commit，fetchone返回的数据就是空。
    row = cursor.fetchone()
    while row:
        print("Insert Product ID :" + str(row[0]))
    row = cursor.fetchone()
    #需要调用commit提交数据，默认不会自动提交。
    conn.commit()
    print("插入数据结束")

# 查询数据
def queryRows(conn):
    print("开始查询数据")
    cursor = conn.cursor()
    cursor.execute("select top 100 * from [dbo].[销售统计表];")
    row = cursor.fetchone()
    while row:
        print("Product ID = " + str(row[0]))
        row = cursor.fetchone()
    print("查询数据结束。")

def queryMaxID(conn):
    cursor = conn.cursor()
    cursor.execute("select MaxId=max(ProductId) from Product;")
    row = cursor.fetchone()
    print("最大的产品ID = " + str(row[0]))

#事务处理
def rollbackTransaction(conn):
    print("开始事务")
    cursor = conn.cursor()
    cursor.execute("begin transaction")
    cursor.execute("insert into Product([Name], ProductNumber) OUTPUT INSERTED.ProductId values('roll back transaction', 'bollback');")
    conn.rollback()
    print("回滚事务")

def main():
    conn = createConnection()
    print("conn",conn)
    # insertRow(conn)
    # print("")
    queryRows(conn)
    # print("")
    # print("事务测试之前")
    # queryMaxID(conn)
    # rollbackTransaction(conn)
    # print("事务测试之后")
    # queryMaxID(conn)
    #closeConnection(conn)
    print("运行完毕。")

if __name__ == '__main__':
    main()