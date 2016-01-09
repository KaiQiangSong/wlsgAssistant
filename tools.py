# coding=utf-8
import urllib;
import urllib2;
import string;

def post(url,para):
    postData = urllib.urlencode(para);
    req = urllib2.Request(url,postData);
    resp = urllib2.urlopen(req);
    return resp;

def get(url):
    req = urllib2.Request(url);
    resp = urllib2.urlopen(req);
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