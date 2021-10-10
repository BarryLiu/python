import contextlib
import pymysql
from pymysql.cursors import DictCursor, Cursor
 
# https://blog.csdn.net/qq_34333481/article/details/109385171
MYSQL_config = {
    'host': "127.0.0.1",
    'port': 8889,
    'database': 'mh',
    'user': 'mh',
    'password': 'dream123',
}

 
class MySQLConnect():
    def __init__(self, cursorclass=DictCursor, config=MYSQL_config):
        self.connection = pymysql.connect(host=config['host'],
                                          port=config['port'],
                                          user=config['user'],
                                          password=config['password'],
                                          db=config['database'],
                                          cursorclass=cursorclass,
                                          charset='utf8mb4'
                                          )
        self.connection.autocommit(True)
 
    # 通过以下两个方法判断mysql是否连通，以及重连。
    def is_connected(self,num=28800,stime=3):  # 重试连接总次数为1天,这里根据实际情况自己设置,如果服务器宕机1天都没发现就......
        _number = 0
        _status = True
        while _status and _number <=num:
            """Check if the server is alive"""
            try:
                self.connection.ping(reconnect=True) #ping 校验连接是否异常
                _status = False
            except:
                if self.re_connect() == True: # 重新连接,成功退出
                    _status = False
                    break
                _number += 1
                time.sleep(stime)  # 连接不成功,休眠3秒钟,继续循环，知道成功或重试次数结束
 
 
 
 
    def re_connect(self):
        try:
            self.connection = pymysql.connect(host=self.MYSQL_config['host'],
                                              port=self.MYSQL_config['port'],
                                              user=self.MYSQL_config['user'],
                                              password=self.MYSQL_config['password'],
                                              db=self.MYSQL_config['db'],
                                              cursorclass=self.cursorclass,
                                              )
            self.connection.autocommit(True)
            return True
        except:
            return False
 
 
 
 
    @contextlib.contextmanager
    def cursor(self, cursor=None):
        """通过yield返回一个curosr对象
        """
        cursor = self.connection.cursor(cursor)
        try:
            yield cursor
        except Exception as err:
            self.connection.rollback()
            raise err
        finally:
            cursor.close()
 
    def close(self):
        self.connection.close()
 
   
 
    def fetchone(self, sql=None):
        self.is_connected()
        if sql:
            with self.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchone()
 
        if self.connection.cursorclass == Cursor:
            return ()
        else:
            return {}
 
    def fetchall(self, sql=None):
        self.is_connected()
        if sql:
            with self.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        return []
 
    def execute(self, sql=None):
        self.is_connected()
        if sql:
            with self.cursor() as cursor:
                return cursor.execute(sql)
 
    def executemany(self, sql=None, data=None):
        self.is_connected()
        if sql and data:
            with self.cursor() as cursor:
                return cursor.executemany(sql, data)
 
 
def get_a_conn(cursorclass=DictCursor):
    return MySQLConnect(cursorclass)


if __name__ == '__main__':
    mysql = get_a_conn()
    sql = 'select version()'
    result = mysql.fetchall(sql)
    for item in result:
        print(item)