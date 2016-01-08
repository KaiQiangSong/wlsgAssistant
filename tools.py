# coding=utf-8
import urllib;
import urllib2;

def post(url,para):
    postData = urllib.urlencode(para);
    req = urllib2.Request(url,postData);
    resp = urllib2.urlopen(req);
    return resp;

def get(url):
    req = urllib2.Request(url);
    resp = urllib2.urlopen(req);
    return resp;
