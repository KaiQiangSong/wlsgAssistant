# coding=utf-8
import operation;
import string;
import time;
import login;
import tools;
import urllib2;
import socket;

time_delay_default = 0;
time_1000_second = 0.001;

def activate_buffs_once(server,pid,pkeys,opener,httpPara):
    if (pid in pkeys):
        resp = operation.activate_general_buffs(server,pid,pkeys[pid],opener,httpPara);
        return resp;
    return 'Has no pkeys';

def activate_buffs_delay(server,pid,num,opener,httpPara):
    #need to do
    for i in range(0,num):
        retryTime = httpPara['retry_time'];
        while (retryTime > 0):
            flag = 0;
            try:
                pkeys = operation.get_general_pkeys(server,opener,httpPara);
                #print pkeys;
                resp = activate_buffs_once(server,pid,pkeys,opener,httpPara);
                print 'Activate General Buffs ( '+pid+' ) :  '+str(i+1);
            except urllib2.URLError as e:
                #print e.errno,e.reason;
                error = e.reason;
                flag = 1;
            except urllib2.HTTPError as e:
                #print e.code,e.reason;
                error = e.reason;
                flag = 1;
            except socket.timeout as e:
                #print 'Time out';
                error = 'Socket Time Out';
                flag = 1;
            if (flag > 0):
                retryTime = retryTime - 1;
            else:
                break;
        # Forward the Exception Error
        if (flag):
            print error;
        time.sleep(time_1000_second * time_delay_default);
    return;

def main_program():
    userList = tools.load_user('user.txt');
    httpPara = tools.load_para('httpPara.txt');
    login.login_all(userList,httpPara);
    num = input(u'Please input the number of the days\n');
    for i in range(0,userList['num']):
        server = userList[str(i)]['server'];
        username = userList[str(i)]['username'];
        password = userList[str(i)]['password'];
        connection = userList[str(i)]['connection'];

        if (connection['error'] != ''):
            print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
            print 'Server :',server;
            print 'User   :',username;
            print 'Login Failed';
            print '\n\n\n';
            continue;
        opener = connection['opener'];

        timer= time.localtime();
        print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
        print 'Server :',server;
        print 'User   :',username;

        resp = activate_buffs_delay(server,'34',num,opener,httpPara);
        resp = activate_buffs_delay(server,'35',num,opener,httpPara);
        resp = activate_buffs_delay(server,'21',num,opener,httpPara);
        resp = activate_buffs_delay(server,'22',num,opener,httpPara);
        resp = activate_buffs_delay(server,'23',num,opener,httpPara);

        print resp;
        print '\n\n\n';
    return;