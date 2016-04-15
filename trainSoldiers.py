# coding=utf-8
import operation;
import string;
import time;
import login;
import tools;
import accelerate;
import urllib2;
import socket;

time_delay_default = 100;
time_1000_second = 0.001;

def train_soldiers_once(server,para,setting,cityID,opener,httpPara):
    if (setting[1] > 0):
        print '骑兵 :'
        limit = operation.get_train_limit(server,setting[1],2,opener,httpPara);
        print '本队列可征:',limit['this'];
        print '全队列可征:',limit['all'];
        if (limit['this'] >= setting[5]):
            resp = operation.train_soldiers(server,setting[1],limit['this'],opener,httpPara).read();
            print resp;
        else:
            print '达不到征兵最低限度!'
        print;
    if (setting[0] > 0):
        print '步兵 :'
        limit = operation.get_train_limit(server,setting[0],1,opener,httpPara);
        print '本队列可征:',limit['this'];
        print '全队列可征:',limit['all'];
        if (limit['this'] >= setting[4]):
            resp = operation.train_soldiers(server,setting[0],limit['this'],opener,httpPara).read();
            print resp;
        else:
            print '达不到征兵最低限度!'
        print;
    if ((para['model'] == 0 or (para['model'] == 1 and cityID == 0)) and (setting[2] > 0)):
        print '攻城车 :'
        limit = operation.get_train_limit(server,setting[2],3,opener,httpPara);
        print '本队列可征:',limit['this'];
        print '全队列可征:',limit['all'];
        if (limit['this'] >= setting[6]):
            resp = operation.train_soldiers(server,setting[2],limit['this'],opener,httpPara).read();
            print resp;
        else:
            print '达不到征兵最低限度!'
        print;
    if (setting[3] > 0):
        print '特殊兵种 :'
        limit = operation.get_train_limit(server,setting[3],4,opener,httpPara);
        print '本队列可征:',limit['this'];
        print '全队列可征:',limit['all'];
        if (limit['this'] >= setting[7]):
            resp = operation.train_soldiers(server,setting[3],limit['this'],opener,httpPara).read();
            print resp;
        else:
            print '达不到征兵最低限度!'
        print;
    return;

def train_soldier_delay(server,para,setting,cityID,opener,httpPara):
    retryTime = httpPara['retry_time'];
    while (retryTime > 0):
        flag = 0;
        try:
            train_soldiers_once(server,para,setting,cityID,opener,httpPara);
            accelerate.accelerate_military(server,para,opener,httpPara);
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
    time.sleep(time_1000_second * para['time_delay']);
    return;

def change_Soldiers_once(server,setting,opener,httpPara):
    soldiers = operation.get_change_Soldiers(server,opener,httpPara);
    if (setting[8] > 0):
        print 'Change1';
        sid = str(setting[8]);
        num = (soldiers[sid] / 100 - setting[9]) * 100;
        if (num > 0):
            num = str(num);
            resp = operation.change_Soldiers(server,sid,num,opener,httpPara);
            resp = resp.read();
            print resp;
    if (setting[10] > 0):
        print 'Change2';
        sid = str(setting[10]);
        num = (soldiers[sid] / 100 - setting[11]) * 100;
        if (num > 0):
            num = str(num);
            resp = operation.change_Soldiers(server,sid,num,opener,httpPara);
            resp = resp.read();
            print resp;
    if (setting[12] > 0):
        print 'Change3';
        sid = str(setting[12]);
        num = (soldiers[sid] / 100 - setting[13]) * 100;
        if (num > 0):
            num = str(num);
            resp = operation.change_Soldiers(server,sid,num,opener,httpPara);
            resp = resp.read();
            print resp;
    return;

def change_Soldiers_delay(server,settings,opener,httpPara):
    retryTime = httpPara['retry_time'];
    while (retryTime > 0):
        flag = 0;
        try:
            change_Soldiers_once(server,settings,opener,httpPara);
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

def main_program():
    userList = tools.load_user('user.txt');
    settings = tools.load_settings('settings_trainSoldiers.txt',14);
    para = tools.load_para('para_trainSoldiers.txt');
    httpPara = tools.load_para('httpPara.txt');
    login.login_all(userList,httpPara);
    timeStep = para['time_change_soldiers'];
    timeStart = 0;
    #print timeStart;
    while(1):
        flag = 0;
        for i in range(0,userList['num']):
            setting = settings[i];
            server = userList[str(i)]['server'];
            username = userList[str(i)]['username'];
            connection = userList[str(i)]['connection'];
            if (connection['error'] != ''):
                timer = time.localtime();
                print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
                print 'Server :',server;
                print 'User   :',username;
                print 'Login Failed';
                print '\n\n\n';
                continue;
            flag = 1;
            opener = connection['opener'];

            #timer= time.localtime();
            #print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
            #print 'Server :',server;
            #print 'User   :',username;


            #print time.time();
            citys = operation.get_citys(server,opener,httpPara);
            for j in range(0,citys['num']):
                timer= time.localtime();
                print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
                print 'Server :',server;
                print 'User   :',username;
                print 'City  :',j;
                x = citys[str(j)]['x'];
                y = citys[str(j)]['y'];
                operation.switch(server,x,y,opener,httpPara);
                train_soldier_delay(server,para,setting,j,opener,httpPara);
                print '\n\n\n';
        if (flag == 0):
            break;
        timeNow = time.time();
        if (timeNow - timeStart > timeStep):
            timeStart = timeNow;
            for i in range(0,userList['num']):
                setting = settings[i];
                server = userList[str(i)]['server'];
                username = userList[str(i)]['username'];
                connection = userList[str(i)]['connection'];

                if (connection['error'] != ''):
                    timer = time.localtime();
                    print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
                    print 'Server :',server;
                    print 'User   :',username;
                    print 'Login Failed';
                    print '\n\n\n';
                    continue;
                #flag = 1;
                opener = connection['opener'];
                citys = operation.get_citys(server,opener,httpPara);
                for j in range(1,citys['num']):
                    timer= time.localtime();
                    print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
                    print 'Server :',server;
                    print 'User   :',username;
                    print 'City  :',j;
                    x = citys[str(j)]['x'];
                    y = citys[str(j)]['y'];
                    operation.switch(server,x,y,opener,httpPara);
                    change_Soldiers_delay(server,setting,opener,httpPara);
                    print '\n\n\n';
    return 0;
