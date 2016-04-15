# coding=utf-8
import operation;
import string;
import time;
import login;
import tools;
import urllib2;
import socket;

time_delay_default = 100;
time_1000_second = 0.001;

def main_program():
    userList = tools.load_user('user.txt');
    httpPara = tools.load_para('httpPara.txt');
    login.login_all(userList,httpPara);
    for i in range(0,userList['num']):
        server = userList[str(i)]['server'];
        username = userList[str(i)]['username'];
        password = userList[str(i)]['password'];
        connection = userList[str(i)]['connection'];
        timer= time.localtime();

        if (connection['error'] != ''):
            print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
            print 'Server :',server;
            print 'User   :',username;
            print 'Login Failed';
            print '\n\n\n';
            continue;
        opener = connection['opener'];

        print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
        print 'Server :',server;
        print 'User   :',username;
        citys = operation.get_citys(server,opener,httpPara);
        print citys;
        print '\n\n\n';