# coding=utf-8
import urllib;
import urllib2;
import cookielib;
import json;
import os;
import socket;

def login(username,password,server,paraHTTP):
	# First url request
	url_login = 'https://passport.9wee.com/login';
	cookielib.Absent();
	file_name = server+'|'+username+'.txt';
	error = '';
	if (os.path.exists(file_name)):
		cj = cookielib.MozillaCookieJar();
		cj.load(file_name, ignore_discard=True, ignore_expires=True)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
		if (check_login(server,opener,paraHTTP) < 0):
			cj = cookielib.MozillaCookieJar(file_name);
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
			retryTime = paraHTTP['retry_time'];
			while (retryTime > 0):
				flag = 0;
				try:
					resp = opener.open(url_login,timeout = paraHTTP['timeout']);
				except urllib2.URLError as e:
					#print e.errno,e.reason;
					error = e.reason;
					flag = 1;
				except urllib2.HTTPError as e:
					#print e.code,e.reason;
					error = e.reason;
					flag = 1;
				except socket.timeout as e:
					print 'Time out';
					e = 'Socket Time Out';
					flag = 1;
				if (flag > 0):
					retryTime = retryTime - 1;
				else:
					break;
			# Forward the Exception Error
			if (flag):
				result = {
					'cj' : cj,
					'opener' : 'opener',
					'error' : error
				};
				return result;
			para = {
				"username": username,
				"password": password
			};
			postData = urllib.urlencode(para);

			retryTime = paraHTTP['retry_time'];
			while (retryTime > 0):
				flag = 0;
				try:
					resp = opener.open(url_login,postData,timeout = paraHTTP['timeout']);
				except urllib2.URLError as e:
					#print e.errno,e.reason;
					error = e.reason;
					flag = 1;
				except urllib2.HTTPError as e:
					#print e.code,e.reason;
					error = e.reason;
					flag = 1;
				except socket.timeout as e:
					print 'Time out';
					e = 'Socket Time Out';
					flag = 1;
				if (flag > 0):
					retryTime = retryTime - 1;
				else:
					break;
			# Forward the Exception Error
			if (flag):
				result = {
					'cj' : cj,
					'opener' : 'opener',
					'error' : error
				};
				return result;
			resp = get_main(server,opener,paraHTTP);
			cj.save(ignore_discard=True, ignore_expires=True);
			if (check_login(server,opener,paraHTTP) < 0):
				error = 'Login Failed';
	else:
		cj = cookielib.MozillaCookieJar(file_name);
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
		retryTime = paraHTTP['retry_time'];
		while (retryTime > 0):
			flag = 0;
			try:
				resp = opener.open(url_login,timeout = paraHTTP['timeout']);
			except urllib2.URLError as e:
				#print e.errno,e.reason;
				error = e.reason;
				flag = 1;
			except urllib2.HTTPError as e:
				#print e.code,e.reason;
				error = e.reason;
				flag = 1;
			except socket.timeout as e:
				print 'Time out';
				e = 'Socket Time Out';
				flag = 1;
			if (flag > 0):
				retryTime = retryTime - 1;
			else:
				break;
		# Forward the Exception Error
		if (flag):
			result = {
				'cj' : cj,
				'opener' : 'opener',
				'error' : error
			};
			return result;

		# Second time do url Request, the CookieJar will auto handle the cookie
		#username = username.encode('utf-8');
		para = {
		"username": username,
		"password": password
		};
		postData = urllib.urlencode(para);
		retryTime = paraHTTP['retry_time'];
		while (retryTime > 0):
			flag = 0;
			try:
				resp = opener.open(url_login,postData,timeout = paraHTTP['timeout']);
			except urllib2.URLError as e:
				#print e.errno,e.reason;
				error = e.reason;
				flag = 1;
			except urllib2.HTTPError as e:
				#print e.code,e.reason;
				error = e.reason;
				flag = 1;
			except socket.timeout as e:
				print 'Time out';
				e = 'Socket Time Out';
				flag = 1;
			if (flag > 0):
				retryTime = retryTime - 1;
			else:
				break;
		# Forward the Exception Error
		if (flag):
			result = {
				'cj' : cj,
				'opener' : 'opener',
				'error' : error
			};
			return result;
		resp = get_main(server,opener);
		cj.save(ignore_discard=True, ignore_expires=True);
		if (check_login(server,opener,paraHTTP) < 0):
			error = 'Login Failed';

	result = {
		'cj' : cj,
		'opener' : opener,
		'error' : error
	};
	return result;


def get_main(server,opener,paraHTTP):
	url_main = 'http://'+server+'.sg.9wee.com/main.php';
	#req = urllib2.Request(url_main);
	#resp = urllib2.urlopen(req);
	retryTime = paraHTTP['retry_time'];
	while (retryTime > 0):
		flag = 0;
		try:
			resp = opener.open(url_main,timeout = paraHTTP['timeout']);
		except urllib2.URLError as e:
			#print e.errno,e.reason;
			error = e.reason;
			flag = 1;
		except urllib2.HTTPError as e:
			#print e.code,e.reason;
			error = e.reason;
			flag = 1;
		except socket.timeout as e:
			print 'Time out';
			e = 'Socket Time Out';
			flag = 1;
		if (flag > 0):
			retryTime = retryTime - 1;
		else:
			break;
	# Forward the Exception Error
	if (flag):
		return error;
	return resp;

def check_login(server,opener,paraHTTP):
	resp = get_main(server,opener,paraHTTP);
	message = resp.read();
	text = u'抵制不良游戏 拒绝盗版游戏 注意自我保护 谨防受骗上当 适度游戏益脑 沉迷游戏伤身 合理安排时间 享受健康生活';
	text = text.encode('utf-8');
	return message.find(text);

def login_all(userList,paraHTTP):
	for i in range(0,userList['num']):
		username = userList[str(i)]['username'];
		password = userList[str(i)]['password'];
		server = userList[str(i)]['server'];
		connection = login(username,password,server,paraHTTP);
		userList[str(i)]['connection'] = connection;
	return userList;