# coding=utf-8
import urllib;
import urllib2;
import string;

def post(url,para,opener):
    postData = urllib.urlencode(para);
    #req = urllib2.Request(url,postData);
    #resp = urllib2.urlopen(req);
    resp = opener.open(url,postData);
    return resp;

def get(url,opener):
    #req = urllib2.Request(url);
    #resp = urllib2.urlopen(req);
    resp = opener.open(url);
    return resp;

def load_para(file_name):
    input = open(file_name,'r');
    settings = input.read();
    input.close();
    #print settings;
    settings = settings.replace('=',' ');
    settings = settings.replace('\n',' ');
    #print settings;
    attr = settings.split();
    #print attr;
    num_attr = len(attr)/2;
    para = {};
    for i in range(0,num_attr):
        para[attr[i*2]] = string.atoi(attr[i*2+1]);
    #para = transport.presetting0();
    return para;

def load_paraString(file_name):
    input = open(file_name,'r');
    settings = input.read();
    input.close();
    #print settings;
    settings = settings.replace('=',' ');
    settings = settings.replace('\n',' ');
    #print settings;
    attr = settings.split();
    #print attr;
    num_attr = len(attr)/2;
    para = {};
    for i in range(0,num_attr):
        para[attr[i*2]] = attr[i*2+1];
    #para = transport.presetting0();
    return para;

def load_user(file_name):
    #input = codecs.open(file_name,'r','utf-8');
    input = open(file_name,'r');
    lines = input.readlines();
    userlist = {};
    userlist['num'] = len(lines);
    for i in range(0,userlist['num']):
        lines[i] = lines[i].split('|');
        user = {};
        user['server'] = lines[i][0];
        user['username'] = lines[i][1];
        user['password'] = lines[i][2];
        userlist[str(i)] = user;
        del user;
    input.close();
    return userlist;