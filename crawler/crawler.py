#encoding=utf-8
import sys,requests,re,time,threading;
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
from function import handle
sys.path.append("..")
from core import CORE;
from mysql.DB import DB;

class crawler(object):
	"""爬虫"""
	
	crawler_progress = []; #爬虫进展
	header3 = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Connection':'keep-alive',
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'};
						
	def __init__(self,tables,url): 
		
		print url,'----->Being crawler ! ^_^';
		crawler.p_get_text(url,tables)

		
	@classmethod
	def p_get_text(cls,url,tables): #获取源码中的a标签
		try:
			r = requests.get("http://"+url,headers=crawler.header3,timeout=10);  
			html_a = r.text.encode('utf-8'); 
			
			soup = BeautifulSoup(html_a)
			html_a = soup.find_all("a");
		except Exception,e:
			try:
				r = requests.get("http://"+url,headers=crawler.header3,timeout=10);  
				html_a = r.text.encode('utf-8'); 
				
				soup = BeautifulSoup(html_a)
				html_a = soup.find_all("a");
			except Exception,e:
				html_a = [];
		if len(html_a) > 0:
			
			for link in html_a:
				a_href = str(link.get('href'));

				strinfo = re.compile("/+")
				a_href = strinfo.sub('/',a_href) #把 多个 "/" 替换成 / 当然 http:// 变成了http:/了

				strinfo = re.compile("http:/")
				a_href = strinfo.sub('http://',a_href)#将http:/ 变成 http://

				strinfo = re.compile("https:/")
				a_href = strinfo.sub('https://',a_href)#将http:/ 变成 http://

				strinfo = re.compile("/+$")
				a_href = strinfo.sub('',a_href) #把最后的 / 删掉

				strinfo = re.compile("#+")
				a_href = strinfo.sub('#',a_href) #把多个# 替换成#
				
				#print a_href
				print a_href;
				if a_href != "/" and a_href != "#" and  a_href != "" and not re.findall("^javascript:",a_href): 
					A = handle(a_href,tables,url);
					
			
		else:
			return False;

			
	






