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


def activate_vip_withCheck(server,vipType,opener,httpPara):
    info = operation.get_vip_info(server,opener,httpPara);
    if (str(info['vType']) == vipType):
        return 'Satisfied';
    resp = operation.activate_vip(server,vipType,opener,httpPara);
    resp = resp.read();
    if (resp.find('VIP激活成功！') != -1):
        return 'Done';
    else:
        return 'Failed';
    return 'Error';


def main_program():
    vipType = raw_input('Please input the type of VIP (136,137):\n');
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
        resp = activate_vip_withCheck(server,vipType,opener,httpPara);
        print resp;
