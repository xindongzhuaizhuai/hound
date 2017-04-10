#-*-coding:utf-8 -*-
import time,threading,sys,core,dns.resolver,os,re;
from  mysql.DB import DB;
from table.tabulate import tabulate
from table.picture import *


def process(fenc,canshu): #导入字典并且还要加载进展条
	output = sys.stdout;
	t = threading.Thread(target=fenc,args=[canshu]); #函数名称
	t.start();
	a = "。";
	while True:
		if t.isAlive():
			x = output.write("\033[5;32;1m Import, may take a few minutes √ %s \r \033[0m" % a);
			output.flush()
			if len(a) > 10:
				a = "。";
				output.flush();
	  			time.sleep(1);
			else:
				a = a+"。";
				output.flush();
	  			time.sleep(1);
  		else:
  			print '                                                                           \r \n ok';
  			break;
  

def im_url(file_url,tables):
	if not os.path.exists(file_url):
		print '\033[1;31;1m   Sorry, the file does not exist.    \033[0m';
		exit();
	else:
		im_url_db = DB();
		sql = "select count(table_name) from information_schema.tables where table_name = '%s' and TABLE_SCHEMA = '%s'" % (tables,core.CORE.db)
  		if im_url_db.query(sql):
  			for url in open(file_url):
  				url = url.replace('http://','').replace('https://','').replace('\r','').replace('\n','');
  				im_resolver=dns.resolver.Resolver();
				im_resolver.nameservers=core.default_dns
				try:
					ip=im_resolver.query(url,'A')[0];
				except Exception,e:
					ip = False;
				if ip != False:
					sql = "select count(id) from %s where url = '%s' " % (tables,url);
					if not im_url_db.query(sql):
						sql = "insert into %s values (null,'%s','%s','0',0,0,'null','null','null',0)" % (tables,url,str(ip));
						im_url_db.increase(sql);
						print url,"===>OK",ip;


  				



def table_print(tables): #表格
	
	a = DB().query_all("desc %s" % (tables));
	table_top = [];

	for x in a:
		table_top.append(x[0])


	b = DB().query_all("select * from %s" % (tables) );


	table_lis = [];
	for x in b:
		table_lis.append(x)


	print tabulate(table_lis, table_top, tablefmt="grid")


def Loop_acquisition_IP():
	
	for url in core.Blacklist_url:
		my_resolver=dns.resolver.Resolver();
		my_resolver.nameservers=core.default_dns
		# 需要查询的域名
		try:
			ip=my_resolver.query(url,'A')[0];
		except Exception,e:
			ip = False;
		
		if ip != False and  not core.Blacklist_ip.count(ip):
			core.Blacklist_ip.append(ip);

def ydns(domain):
	try:
		res = os.popen('nslookup -type=ns ' + domain).read()
		nameserver = re.findall(r'nameserver = ([\w\.]+)',res)
		for server in nameserver:
		    #print server+">>>>>>>>>>>>>>>>>>>>>>>>>>>";
		    if len(server) < 5:
		        server += domain
		    res = os.popen('dig axfr @%s %s' % (server,domain)).read()
		    yuming =  re.findall(r"([A-Za-z0-9\_\-\.]+)\s+\d+\s+IN",res);
		    replace_reg = re.compile(r'\.$');

		    if yuming:
				for i,ym  in enumerate(yuming):
					replace_reg = re.compile(r'\.$')
					ym = replace_reg.sub('', ym)
					yuming[i] = ym;
				return  yuming;
	except Exception,e:
		yuming = False;
		return  yuming;


def ip(url):
	my_resolver=dns.resolver.Resolver();
	my_resolver.nameservers=core.default_dns
	# 需要查询的域名
	try:
		ip=my_resolver.query(url,'A')[0];
	except Exception,e:
		ip = False;
	
	if ip != False and  not core.Blacklist_ip.count(ip):
		return ip;
	else:
		return '0.0.0.0';

