# -*- coding:utf-8 -*-
import sys,time,socket;
sys.path.append("..")
import core;
class DB(core.CORE):
	'操作mysql简单增删改查'
	
	def increase(self,sql): #增 删 改 数据方法
		try:
			self.mysql.execute(sql); #操作数据
			self.db.commit();#提交数据
		except Exception,e:
		    print '\033[1;31;1m'+"function: increase --> Mysql Error: %s" % (e) + '\033[0m';
		    exit();

	def query(self,sql): #查询一条
		try:
			self.mysql.execute(sql); #查询数据
			q_db = self.mysql.fetchone(); 
		
			return q_db[0]
		except Exception,e:
			print '\033[1;31;1m'+"function: query --> Exception: %s  Error: %s " % (Exception,e) +'\033[0m';
			exit();


	def Dictionaries(self,Dir):  #批量导入字典方法
		try:
			f = open(Dir,'r')
			sql = "select count(table_name) from information_schema.tables where table_name = 'lis' and TABLE_SCHEMA = '%s'" % (core.CORE.db);
			self.mysql.execute(sql); #查询数据
			q_db = self.mysql.fetchone(); 
			if not q_db[0]:
				
				sql = """
					create table lis(
					id int not null primary key auto_increment,
					lis varchar(20)	not null comment 'zidian'
					)charset utf8 engine = innodb;
				""";
				self.mysql.execute(sql); #操作数据
				self.db.commit();#提交数据
				

			for line in f.readlines():
				line2 = line.strip();#去除换行符
				sql = "insert into lis values(null,\"%s\")" % (line2);
				self.mysql.execute(sql); #操作数据
				self.db.commit();#提交数据

				time.sleep(0.01);
			f.close() #关闭
		except Exception,e:
			print '\033[1;31;1m'+"function: Dictionaries --> Exception: %s  Error: %s " % (Exception,e) +'\033[0m';
			exit();

	def  Domain_storage(self,tables,url,ip): #域名入库
		try:
			sql = "select count(ip) from %s where ip = '%s'" % (tables,ip);
			self.mysql.execute(sql); #查询数据
			q_db = self.mysql.fetchone(); 
			if q_db[0] >= 15 :
				core.Blacklist_ip.append(ip);
			else:
				sql = "select count(*) from %s where url = '%s'" % (tables,url);
				self.mysql.execute(sql); #查询数据
				q_db = self.mysql.fetchone(); 
				if q_db[0] == 0:#入库之前 先判断数据库是否含有相同信息 如果没有就入裤
					
					sql = "insert into %s values(null,\"%s\",\"%s\",0,0,0,0)" % (tables,url,ip);
					self.mysql.execute(sql); #操作数据
					self.db.commit();#提交数据

		except Exception,e:
			print '\033[1;31;40m'+"function: Domain_storage --> Exception: %s  Error: %s " % (Exception,e) +'\033[0m';
			return False;



	def query_all(self,sql): #查询所有
		try:
			list_all = self.mysql.execute(sql); #执行sql
			list_all = self.mysql.fetchmany(list_all); #查询所有
			self.db.commit();#提交数据
			return list_all
		except Exception,e:
			print '\033[1;31;1m'+"function: query_all --> Exception: %s  Error: %s " % (Exception,e) +'\033[0m';
			exit();





######################爬虫#########################################

	def p_increase(self,sql): #增 删 改 数据方法
		try:
			self.mysql.execute(sql); #操作数据
			self.db.commit();#提交数据
		except Exception,e:
			print '\033[1;31;1m'+"function: p_increase --> Exception: %s  Error: %s " % (Exception,e) +'\033[0m';



