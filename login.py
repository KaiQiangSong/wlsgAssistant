# coding=utf-8
import urllib;
import urllib2;
import cookielib;
import json

def login(username,password,server):
	# First url request
	url_login = 'https://passport.9wee.com/login';
	cookielib.Absent();
	cj = cookielib.CookieJar();
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
	urllib2.install_opener(opener);
	resp = opener.open(url_login);

	# Second time do url Request, the CookieJar will auto handle the cookie
	#username = username.encode('utf-8');

	#username = username.encode('utf-8');
	para = {
	"username": username,
	"password": password
	}

	#print para;

	postData = urllib.urlencode(para);
	resp = opener.open(url_login,postData);
	resp = get_main(server,opener);
	result = {
		'cj' : cj,
		'opener' : opener,
		'resp' : resp
	};
	return result;


def get_main(server,opener):
	url_main = 'http://'+server+'.sg.9wee.com/main.php';
	#req = urllib2.Request(url_main);
	#resp = urllib2.urlopen(req);
	resp = opener.open(url_main);
	#result = resp.read();
	return resp;

def check_login(server):
	resp = get_main(server);
	message = resp.read();
	text = u'抵制不良游戏 拒绝盗版游戏 注意自我保护 谨防受骗上当 适度游戏益脑 沉迷游戏伤身 合理安排时间 享受健康生活';
	text = text.encode('utf-8');
	return message.find(text);

def login_all(userList):
	for i in range(0,userList['num']):
		username = userList[str(i)]['username'];
		password = userList[str(i)]['password'];
		server = userList[str(i)]['server'];
		connection = login(username,password,server);
		userList[str(i)]['connection'] = connection;
	return userList;