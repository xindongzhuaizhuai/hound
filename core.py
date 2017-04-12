# -*- coding:utf-8 -*-
import MySQLdb;
default_dns = [
	'8.8.8.8',
	'8.8.4.4'];

Blacklist_url=[
'dflkjadlfkjasldf.qq.com',
'dflkjadlfk2.youku.com',
'dflkjadlfk2.163.com',
'dflkjadlfk2.tudou.com'
]

Blacklist_ip=[1];

class CORE():
	
	'mysql 登录'
	host = '127.0.0.1';
	user = 'root';
	passwd = '123456';
	db = 'hound';
	port = 3306;
	charset = 'utf-8';

	def __init__(self):
		try:
			self.db=MySQLdb.connect(host=CORE.host,user=CORE.user,passwd=CORE.passwd,charset='utf8'); #登录数据库
			self.mysql = self.db.cursor();
		   	sql = "select schema_name from information_schema.schemata where schema_name='%s'" % (CORE.db);
		   	self.mysql.execute(sql);


		   	if not self.mysql.fetchone():
		   		sql = "CREATE DATABASE IF NOT EXISTS %s " % (CORE.db);
		   		self.mysql.execute(sql);
		   		self.db.select_db(CORE.db) #选择数据库
		   		
		   		
		   	else:
		   		self.db.select_db(CORE.db) #选择数据库
		   		
		   		
		except Exception,e:
		    print'\033[1;31;1m'+"Mysql Error: %s" % (e) + '\033[0m';
		    exit();
