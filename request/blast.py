# -*- coding=utf-8 -*-
import threading,sys,time,datetime;
sys.path.append("..")
from mysql.DB import DB;
from request.simple import simple 
import function;
class blast(simple):
	xiancheng = [];
	"""爆破域名"""
	def blast_url(self,url,t,lis,tables):
		progress = sys.stdout;
		#lis = DB().query_all("select lis from lis"); #字典数据
		total = len(lis) #获取字典总数
		blast_i = []; #获取线程是否结束
		fenliang = total / t;  #总数除以线程 得到每份数量
		kaishi = 0;
		jiewei = fenliang;
		self.simple = simple();
		print '\033[1;36;1m Is finishing the dictionary, ready to send all requests \r \033[0m';
		
		function.Loop_acquisition_IP(); #爆破之前 先获取黑名单IP
		while True:
			list2 = lis[kaishi:jiewei]; #获取成员份量
			t = threading.Thread(target=self.simple.h_get_blast_text,args=[url,list2,tables]); #判断是否存在域名 如果有就入库 表名是url的值
			t.start();
			blast_i.append(t)
			
			if jiewei > total:
				break;

			kaishi = kaishi + fenliang;
			jiewei = jiewei + fenliang;
			time.sleep(0.02);
		
		print '\033[1;36;1m All requests are sent, waiting for a response. √ \r \033[0m'
		
		inhour = 5; 
		for x in xrange(5):

			progress.write('\033[1;36;1m Still need to wait %i \r \033[0m' % inhour);
			progress.flush();
			inhour = inhour - 1;
			time.sleep(1);
		print '\r \n';
		print '\033[1;36;1m Need a little time ..... \r\n \033[0m'
		print '\n '

		for xx in blast_i:
			while True:
				if not xx.isAlive():
					break;	
				else:
					progress.write("\033[1;32;1m mdomain: %s ----total: %i , ----Already request:%i  \r \033[0m" % (url,total,simple.walk) );
					progress.flush();
					time.sleep(0.12);


		print ' \n \n  The whole process is completed. ^_^'
		print '\n Wait for all requests to end! '
 	   	print '\033[1;36;1m oK,Sorting data √ \033[0m';





 	   	#递归爆破				#表名 线程 字典  批量域名
	def recursion_blast_url(self,tables,t,lis,url_list):
		progress = sys.stdout;
		
		total = len(lis); #请求总数

		
		fenliang = total / t;  #总数除以线程 得到每份数量
		
		kaishi = 0;
		jiewei = fenliang;
		
		self.simple = simple();
		now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		for recursion_url in url_list:
			print " URL:"+recursion_url[0]+"-->\033[1;32;1m  Send out all the requests  Current time:  %s \r \033[0m" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
			while True:
				list2 = lis[kaishi:jiewei]; #获取成员份量
				
				t = threading.Thread(target=self.simple.recursion_h_get_blast_text,args=[recursion_url[0],list2,tables]); #判断是否存在域名 如果有就入库 表名是url的值
				t.start();
				blast.xiancheng.append(t);
				if jiewei > total:
					kaishi = 0;
					jiewei = fenliang
					break;
				else:
					kaishi = kaishi + fenliang;
					jiewei = jiewei + fenliang;
				time.sleep(0.02);

		
		for tt in blast.xiancheng:
		   	tt.join(); #等待所有线程结束
		sql = "update %s set recursion = 1 where url = '%s'" % (tables,recursion_url[0]);
		DB().increase(sql);
		print "\033[1;32;1m  <--Above the domain name to send complete 0o(^_^)o0  Current time: %s \033[0m  \r\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

