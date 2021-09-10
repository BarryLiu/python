# -*- coding:utf-8 -*-

import pymysql,sys,logging

# 打开数据库连接
db = pymysql.connect("192.168.1.65","root","root","bom_real" )

# 初始化logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

fh = logging.FileHandler('../test.log') #写入日志文件 
ch = logging.StreamHandler() # 用于输出到控制台 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # 输出格式formatter
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)


def change_project(pro_id,ver_type,ver_index):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    query = "update t_project set defualt_ver = '{}' where _id = '{}'".format(ver_type,pro_id)
    cursor.execute(query)
    query = "update t_field_config set version_type = '{}',verindex = {} where project_id ={}  ".format(ver_type,ver_index,pro_id)
    cursor.execute(query)
    db.commit()
    pass

def close():
    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    # 第一个参数是项目id ,第二个是版本,第三个是项目版本
    logger.info("project_id=%s,\t version_type=%s verindex=%s"%(sys.argv[1],sys.argv[2],sys.argv[3])) 
    print(sys.argv[1],sys.argv[2],sys.argv[3])
    change_project(sys.argv[1],sys.argv[2],sys.argv[3])
    close()
    print('运行结束')
    pass