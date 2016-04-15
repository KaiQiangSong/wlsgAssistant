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

def citysPrint(citys,output,start,end):
    num = citys['num'];
    start = max(start-1,0);
    end = min(end,num);
    for i in range(start,end):
        x = citys[str(i)]['x'];
        y = citys[str(i)]['y'];
        name = citys[str(i)]['name'];
        output.write(name);
        output.write(' ');
        output.write(str(x));
        output.write('|');
        output.write(str(y));
        output.write('\n');
    return;

def main_program():
    file_name = raw_input('Please input the file name of result:\n');
    start = input('Please input start city: (From 1 to 5)\n');
    end = input('Please input end city(From 1 to 5):\n');
    output = open(file_name,'w');
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
        citysPrint(citys,output,start,end);
    output.close();