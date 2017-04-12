# -*- coding=utf-8 -*-
import requests,re,sys,time,threading,Queue;
import dns.resolver
sys.path.append("..")
from mysql.DB import DB;
import core;
db_plus = DB();
q = Queue.Queue(1);
w = Queue.Queue(1);
class simple(object):
	walk = 0;
	walk2 = 0;
	recursion_walk=0
	"""简单的http请求"""
	def __init__(self):
		self.header2 = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Connection':'keep-alive',
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'};
	def h_get_text(self,url): #获取源码
		try:
			r = requests.get(url,headers=self.header2,timeout=10);  
			return r.text.encode('utf-8'); 
		except Exception,e:
			print'\033[1;31;1m'+"Exception: %s  Error: %s " % (Exception,e) +'\033[0m';
			return '';

	def h_post_text(self,url,canshu): #获取源码
		try:
			r = requests.post(url,headers=self.header2,data=canshu,timeout=7);  
			return r.text.encode('utf-8'); 
		except Exception,e:
			#print'\033[1;31;40m'+"Exception: %s  Error: %s " % (Exception,e) +'\033[0m';
			return '';

	def h_get_isurl(self,tables,url): #接口获取到的域名 然后判断域名是否存在 如果存在就如裤
		try:
			while not q.empty():
				time.sleep(0.1);
			url = url.replace('http://','').replace('https://','');
			i_resolver=dns.resolver.Resolver()
			i_resolver.nameservers=core.default_dns;
			ip = i_resolver.query(url,'A')
			if ip[0] :
				ip = ip[0];
		except Exception,e: #请求超时 说明没有
			ip = False;
		
		if ip and not core.Blacklist_ip.count(ip) : #如果域名存在的话
			w.put(url)
			db_plus.Domain_storage(tables,url,ip); #入裤
			print '\033[1;33;1m   Successful storage  ^_^. \033[0m';
			w.get()
			






##########################循环判断域名是否存在   如果存在就入库#####################
						#		url，字典
	def h_get_blast_text(self,url,lis,tables): #循环判断域名是否存在   如果存在就入库
		this = simple();
		for x in range(len(lis)):
			simple.walk = simple.walk +1;
			h_url = lis[x][0]+"."+url;
			this.is_url(h_url,tables)
			time.sleep(0.5);

	





##########################递归 循环判断域名是否存在   如果存在就入库#####################
	def recursion_h_get_blast_text(self,url,lis,tables): #循环判断域名是否存在   如果存在就入库
		this = simple();
		
		for x in range(len(lis)):
			h_url = lis[x][0]+"."+url;
			this.is_url(h_url,tables);

			
			
			
		# for tt in a:
		#    	tt.join(); #等待所有线程结束


	def is_url(self,url,tables):
		try:
			url = url.replace('http://','').replace('https://','');
			resolver=dns.resolver.Resolver()
			resolver.nameservers=core.default_dns;
			ip = resolver.query(url,'A')
			if ip[0] :
				ip = ip[0];
		except Exception,e: #如果没有
			
			ip = False;
			
		if ip and not core.Blacklist_ip.count(ip): #如果域名存在的话 and IP不是黑名单的话
			while not q.empty():
				time.sleep(0.1);

			q.put(url)
			tables = tables.replace('.','_');
			db_plus.Domain_storage(tables,url,ip); #入裤
			q.get()
