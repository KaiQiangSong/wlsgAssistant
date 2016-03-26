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

def accelerate_military(server,para,opener):
    pkeys = operation.get_accelerate_pkeys(server,opener);
    if (para['bu_acc'] > 0):
        print '步兵';
        num = operation.get_queue_num_BuBing(server,opener);
        print '队列数:',num;
        for i in range(0,num):
            resp = operation.accelerate_military(server,17,pkeys['17'],i,opener);
            resp = resp.read();
            if (resp.find('激活成功！') == -1):
                resp = '当前城池没有征募兵任务，或最少10秒一个';
            else:
                resp = '激活成功！';
            print '队列',i,':',resp;
    if (para['qi_acc'] > 0):
        print '骑兵';
        num = operation.get_queue_num_QiBing(server,opener);
        print '队列数:',num;
        for i in range(0,num):
            resp = operation.accelerate_military(server,18,pkeys['18'],i,opener);
            resp = resp.read();
            if (resp.find('激活成功！') == -1):
                resp = '当前城池没有征募兵任务，或最少10秒一个';
            else:
                resp = '激活成功！';
            print '队列',i,':',resp;
    if (para['che_acc'] > 0):
        print '攻城车';
        num = operation.get_queue_num_GongCheng(server,opener);
        print '队列数:',num;
        for i in range(0,num):
            resp = operation.accelerate_military(server,19,pkeys['19'],i,opener);
            resp = resp.read();
            if (resp.find('激活成功！') == -1):
                resp = '当前城池没有征募兵任务，或最少10秒一个';
            else:
                resp = '激活成功！';
            print '队列',i,':',resp;
    if (para['te_acc'] > 0):
        print '特殊兵种';
        num = operation.get_queue_num_TeShu(server,opener);
        print '队列数:',num;
        for i in range(0,num):
            resp = operation.accelerate_military(server,20,pkeys['20'],i,opener);
            resp = resp.read();
            if (resp.find('激活成功！') == -1):
                resp = '当前城池没有征募兵任务，或最少10秒一个';
            else:
                resp = '激活成功！';
            print '队列',i,':',resp;
    time.sleep(time_1000_second * para['time_delay'])
    return ;

def accelerate_building(server,para,opener):
    info = operation.get_building_information(server,opener);
    if (info == "无在建建筑"):
        print "无在建建筑";
    elif (para['model_acc'] > 0):
        sids = operation.get_build_sids(server,info['queue_id'],opener);
        if (info['need_time'] < 3600):
            if (sids['model'] > 0):
                resp = operation.accelerate_building(server,info['queue_id'],sids['33'],opener);
            else:
                resp = operation.accelerate_building(server,info['queue_id'],sids['30'],opener);
        elif (info['need_time'] < 16200):
            if (sids['model'] > 0):
                resp = operation.accelerate_building(server,info['queue_id'],sids['32'],opener);
            else:
                resp = operation.accelerate_building(server,info['queue_id'],sids['29'],opener);
        elif (info['need_time'] < 25200):
            if (sids['model'] > 0):
                resp = operation.accelerate_building(server,info['queue_id'],sids['31'],opener);
            else:
                resp = operation.accelerate_building(server,info['queue_id'],sids['28'],opener);
        else:
            if (sids['model'] > 0):
                resp = operation.accelerate_building(server,info['queue_id'],sids['13'],opener);
            else:
                resp = operation.accelerate_building(server,info['queue_id'],sids['12'],opener);
        print resp.read();
    return;

def accelerate_technology_once(server,opener,httpPara):
    pkeys = operation.get_accelerate_pkeys(server,opener,httpPara);
    resp = operation.accelerate_research(server,'14',pkeys['14'],opener,httpPara);
    print resp.read();
    resp = operation.accelerate_research(server,'15',pkeys['15'],opener,httpPara);
    print resp.read();
    resp = operation.accelerate_research(server,'16',pkeys['16'],opener,httpPara);
    print resp.read();
    return ;

def accelerate_technology_delay(server,opener,httpPara):
    retryTime = httpPara['retry_time'];
    while (retryTime > 0):
        flag = 0;
        try:
            accelerate_technology_once(server,opener,httpPara);
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
    return ;


def accelerate_once(server,para,opener):
    return ;

def main_program():
    userList = tools.load_user('user.txt');
    httpPara = tools.load_para('httpPara.txt');
    login.login_all(userList,httpPara);
    while(1):
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

            accelerate_technology_delay(server,opener,httpPara);
            print '\n\n\n';