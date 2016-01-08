# coding=utf-8
import urllib;
import urllib2;
import cookielib;
import json

def login(username,password):
	# First url request
	url_login = 'https://passport.9wee.com/login';
	cookielib.Absent();
	cj = cookielib.CookieJar();
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
	urllib2.install_opener(opener);
	resp = urllib2.urlopen(url_login);

	# Second time do url Request, the CookieJar will auto handle the cookie
	#username = username.encode('utf-8');

	para = {
	"username": username,
	"password": password
	}

	#print para;

	postData = urllib.urlencode(para);
	req = urllib2.Request(url_login,postData);

	resp = urllib2.urlopen(req);
	#result = resp.info();
	return resp;


def get_main(server):
	url_main = 'http://'+server+'.sg.9wee.com/main.php';
	req = urllib2.Request(url_main);
	resp = urllib2.urlopen(req);
	result = resp.read();
	return resp;

def check_login(server):
	resp = get_main(server);
	message = resp.read();
	text = u'忘记密码';
	text = text.encode('utf-8');
	return message.find(text);
