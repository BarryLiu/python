import logging,pymssql,requests,time
import collections
"""
	生产服务器上面有些脏数据,写程序修复一下.
	之前程序bug导致表[dbo].[销售统计表] 里面id 1762663  2019922 区间的 国籍字段数据不正确，
	通过淘宝提供的接口（http://ip.taobao.com/service/getIpInfo.php?ip=01.01.01.01） 获取到这些数据的国籍进行修改
"""

# 初始化连接
conn = pymssql.connect(server='192.168.1.65', user='sa', password='Wheatek!', database='OTA')

# 初始化logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

fh = logging.FileHandler('./test.log') #写入日志文件 
ch = logging.StreamHandler() # 用于输出到控制台 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # 输出格式formatter
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)


def get_ip_country(ip):
	'''通过传入ip返回这个ip所在的国家'''
	try:
		req = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s'%ip)
		json = req.json()
		country = json['data']['country']
		assert country !=''
		return country
	except Exception as e:#如果出异常了休息10秒钟再请求，直到请求成功为止
		logger.error('请求出错了,等10秒钟再请求-----------------',e)
		time.sleep(10)
		return get_ip_country(ip)


	

def query_idandip(start,end): 
	sql = "select top %d * from [dbo].[销售统计表] where 1=1 and id >=%d ;"%((end-start),start)
	logger.info("sql=%s,\tstart=%d,end=%d"%(sql,start,end)) 
	cursor = conn.cursor()
	cursor.execute(sql)
	row = cursor.fetchone()
	items=[]
	while row:
		#print("Product ID = " + str(row[0])+'__'+str(row[1]))
		it=Item(id=row[0],ip=row[1],country=None)
		items.append(it)
		row = cursor.fetchone()
	print("查询数据结束。")
	return items



# start_id = 1762663

start_id = 1767262
end_id = 2019922

#limits = list(range(start_id,end_id,100))
#print(limits)


# item = collections 
Item = collections.namedtuple('Item', ['id', 'ip','country'])


for start in range(start_id,end_id,100):
	end = start+100
	# 如果最后一个id大于endid,则让他等于endid
	if end > end_id: end = end_id  
	logger.warning('id limit %d,%d'%(start,end))

	items = query_idandip(start,end)
	print('items.len=%d'%len(items))
	print(items)
	cursor = conn.cursor()
	for id,ip,country in items:
		time.sleep(0.1)
		country=get_ip_country(ip)
		#update_data_city(id,ip,country)
		sql = "update [dbo].[销售统计表] set 国籍='%s' where id = %d"%(country,id)
		logger.warning(sql)
		cursor.execute(sql)
	conn.commit()
	logger.error("id区间为%d到%d的数据修改成功!"%(start,end));
	pass
conn.close()
print('程序运行结束') 