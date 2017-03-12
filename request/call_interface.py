# -*- coding=utf-8 -*-
import simple,re,time;

class call_interface(simple.simple):
	"""接口调用"""
	@staticmethod
	def jiekou1(url):#接口1
		try:
			print '\033[1;38;1m Is requesting an interface, the process will be a bit slow \033[0m'
			canshu  = {'b2': 1, 'b3': 1,'b4' : 1,'domain':url}
			html = simple.simple().h_post_text('http://i.links.cn/subdomain/',canshu)
			r = r'<input type=hidden name=[a-z0-9]+ id=[a-z0-9]+ value="([\S]+)">';
			html2 = re.findall(r,html);
			return html2;
		except Exception,e: #如果请求失败 就再请求一次
			try:
				time.sleep(2);
				canshu  = {'b2': 1, 'b3': 1,'b4' : 1,'domain':url}
				html = simple.simple().h_post_text('http://i.links.cn/subdomain/',canshu)
				r = r'<input type=hidden name=[a-z0-9]+ id=[a-z0-9]+ value="([\S]+)">';
				html2 = re.findall(r,html);
				return html2;
			except Exception,e: #如果请求失败 就再请求一次 还失败 就返回空
				try:
					time.sleep(2);
					canshu  = {'b2': 1, 'b3': 1,'b4' : 1,'domain':url}
					html = simple.simple().h_post_text('http://i.links.cn/subdomain/',canshu)
					r = r'<input type=hidden name=[a-z0-9]+ id=[a-z0-9]+ value="([\S]+)">';
					html2 = re.findall(r,html);
					return html2;
				except Exception,e:
					print e;
					aaa = [];
					return aaa;



