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
    input.close();
    userlist = {};
    userlist['num'] = len(lines);
    for i in range(0,userlist['num']):
        lines[i] = lines[i].split();
        user = {
            'server': lines[i][0],
            'username' : lines[i][1],
            'password' : lines[i][2],
        }
        userlist[str(i)] = user;
        del user;
    return userlist;

def load_settings_string(file_name,col):
    input = open(file_name,'r');
    attr = input.read().split();
    input.close();
    num_attr = len(attr);
    row = num_attr / col;
    print num_attr;
    settings= [];
    for i in range(0,row):
        this_attr = [];
        for j in range(0,col):
            k = i * col + j;
            this_attr.insert(j,attr[k]);
        settings.insert(i,this_attr);
        del this_attr;
    return settings;

def load_settings(file_name,col):
    settings = load_settings_string(file_name,col);
    row = len(settings);
    for i in range(0,row):
        for j in range(0,col):
            settings[i][j] = string.atoi(settings[i][j]);
    return settings;