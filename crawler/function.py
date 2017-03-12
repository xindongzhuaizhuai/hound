# -*- coding=utf-8 -*-
import re,sys,socket;
from urlparse import urlparse
sys.path.append("..")
from mysql.DB import DB;
from request.simple import simple;
"""
URL: print list(urlparse("http://www.baidu.com/s/index.php?id=1&name=liu#111"))
[0] == scheme -> scheme='http',
[1] == netloc -> netloc='www.baidu.com',
[2] == path -> path='/s/index.php'',
[3] == params -> params='',
[4] == query -> query='id=1&name=liu',
[5] == fragment ->fragment='111'
"""
def handle(url,tables,domain):
	
	url_2 = urlparse(url);
	url = url.replace('http://','').replace('https://','');
	if url_2.netloc != "":  #判断是否有netloc；
		
		if re.search(".%s" % (domain) ,url_2.netloc) != None: #如果相关域名存在的话
			print '\033[1;38;1m  Get a 1 related domain name  %s \033[0m' % (url.split('/')[0]);
			try:
				simple().h_get_isurl(tables,url.split('/')[0]);
			except Exception,e:
				print Exception,e;
			

	

		
		






		
		





