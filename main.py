# coding=utf-8
import urllib,urllib2,cookielib,json;
import threading,time,random;
import login;
import operation;
import transport;
import time;
import string;
import tools;
import open_box;
import trainSoldiers;
import accelerate;
import Building;


users = tools.load_user('user.txt');
print users;


login.login_all(users);
#print users['1']['connection']['cj'];

cj = users['1']['connection']['cj'];
for item in cj:
    print item.name,':',item.value;

opener = users['1']['connection']['opener'];
server = users['1']['server'];
resp = login.check_login(server,opener);

print resp;