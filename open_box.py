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

def openBox_once(server,para,pkeys,opener,httpPara):
    city0 = operation.get_city0(server,opener,httpPara);
    resp = operation.get_transport_massages(server,city0['x'],city0['y'],opener,httpPara);
    resp =  resp.read();
    resp = resp.replace(':',' ');
    resp = resp.replace('json=	{',' ');
    resp = resp.replace('}','');
    resp = resp.replace(',',' ');
    resp = resp.split();
    num_attr = len(resp)/2;
    resource = {};
    for j in range(2,num_attr):
        attr = resp[j*2];
        resource[attr] = string.atoi(resp[j*2+1]);
    time.sleep(time_1000_second * para['time_delay']);
    timer = time.localtime();
    print 'Time:'+str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
    print resource['mucai'],resource['nitu'],resource['tiekuang'],resource['liangshi'];
    if (para['model'] == 0):
        if (resource['mucai'] < para['mu']):
            print "Need MuCai";
            resp = operation.open_box(server,5,1,pkeys,opener,httpPara);
            return resp.read();
        if (resource['nitu'] < para['ni']):
            print "Need NiTu";
            resp = operation.open_box(server,5,1,pkeys,opener,httpPara);
            return resp.read();
        if (resource['tiekuang'] < para['tie']):
            print "Need TieKuang";
            resp = operation.open_box(server,5,1,pkeys,opener,httpPara);
            return resp.read();
        if (resource['liangshi'] < para['liang'],opener,httpPara):
            print "Need LiangShi";
            resp = operation.open_box(server,5,1,pkeys,opener,httpPara);
            return resp.read();
    else:
        if (resource['mucai'] < para['mu_percent'] * resource['cangku'] / 100.0):
            print "Need MuCai";
            resp = operation.open_box(server,5,1,pkeys,opener,httpPara);
            return resp.read();
        if (resource['nitu'] < para['ni_percent'] * resource['cangku'] / 100.0):
            print "Need NiTu";
            resp = operation.open_box(server,5,1,pkeys,opener,httpPara);
            return resp.read();
        if (resource['tiekuang'] < para['tie_percent'] * resource['cangku'] / 100.0):
            print "Need TieKuang";
            resp = operation.open_box(server,5,1,pkeys,opener,httpPara);
            return resp.read();
        if (resource['liangshi'] < para['liang_percent'] * resource['liangcang'] / 100.0):
            print "Need LiangShi";
            resp = operation.open_box(server,5,1,pkeys,opener,httpPara);
            return resp.read();
    return "Satisfied";

#def openBox(server,username,password,para,httpPara):
#    connection = login.login(username,password,server,httpPara);
#    while (1):
#        opener = connection['opener'];
#        pkeys = operation.get_openBox_pkeys(server,opener,httpPara);
#        resp = openBox_once(server,para,pkeys,opener,httpPara);
#        print resp;
#        time.sleep(time_1000_second * para['time_delay']);
#    return;



#def main_program():
#    settings = tools.load_para('settings_openBox.txt');
#    para = tools.load_paraString('user_openBox.txt');
#    httpPara = tools.load_para('httpPara.txt');
#    openBox(para['server'],para['username'],para['password'],settings,httpPara);
#    return ;

def openBox_delay(server,para,opener,httpPara):
    #need to do
    retryTime = httpPara['retry_time'];
    while (retryTime > 0):
        flag = 0;
        try:
            pkeys = operation.get_openBox_pkeys(server,opener,httpPara);
            resp = openBox_once(server,para,pkeys,opener,httpPara);
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
        return error;
    time.sleep(time_1000_second * para['time_delay']);
    return resp;

def main_program():
    userList = tools.load_user('user.txt');
    httpPara = tools.load_para('httpPara.txt');
    login.login_all(userList,httpPara);
    paraOpenBox = tools.load_para('settings_openBox.txt');
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

            resp = openBox_delay(server,paraOpenBox,opener,httpPara);
            print resp;
            print '\n\n\n';


def openBox_define(server,username,password,choice,numberBox,httpPara):
    connection = login.login(username,password,server,httpPara);
    opener = connection['opener'];
    for i in range(0,numberBox):
        retryTime = httpPara['retry_time'];
        while (retryTime > 0):
            flag = 0;
            try:
                pkeys = operation.get_openBox_pkeys(server,opener,httpPara);
                print 'OpenBox :',i+1;
                resp = operation.open_box(server,5,choice,pkeys,opener,httpPara);
                resp = resp.read();
                print resp;
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

def main_program_define():
    para = tools.load_paraString('user_openBox.txt');
    httpPara = tools.load_para('httpPara.txt');
    choice = input(u'请输入你想要开箱子的类型：1 资源 2 经验 3 装备\n');
    numberBox = input(u'请输入你想要开箱子的数量：\n');
    openBox_define(para['server'],para['username'],para['password'],choice,numberBox,httpPara);
    return ;