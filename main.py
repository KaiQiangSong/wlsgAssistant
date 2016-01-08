# coding=utf-8
import urllib,urllib2,cookielib,json;
import threading,time,random;
import login;
import operation;
import transport;
import time;
import string;
import codecs;

time_delay_default = 100;
time_1000_second = 0.001;

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

def load_para_transport(file_name):
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

def transport_all(server,username,password,para):
    resp = login.login(username,password);

    while (login.check_login(server) != -1):
        resp = login.login(username, password);
        print resp.read();
        time.sleep(time_1000_second * time_delay_default);
    #para = transport.presetting0();
    resp = transport.transport_once(server,para);
    resp.strip();
    print resp;
    time.sleep(time_1000_second * time_delay_default);
    return;

def main_program():
    userlist = load_user('user.txt');
    para_transport = load_para_transport('settings_transport.txt');
    #print userlist;
    while(1):
        for i in range(0,userlist['num']):
            server = userlist[str(i)]['server'];
            username = userlist[str(i)]['username'];
            password = userlist[str(i)]['password'];
            #time.strftime( ISOTIMEFORMAT, time.localtime(time.time()));
            timer= time.localtime();

            print 'Time   : '+str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
            print 'Server : '+server;
            print 'User   : '+username;
            #print time.time();
            transport_all(server,username,password,para_transport);
            #print time.time();
            print '\n\n\n';
    return 0;

main_program();