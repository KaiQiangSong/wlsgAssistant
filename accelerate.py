# coding=utf-8
import operation;
import string;
import time;
import login;
import tools;

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

def accelerate_technology(server,para,opener):

    return ;


def accelerate_once(server,para,opener):
    return ;

def main_program():
    userList = tools.load_user('user.txt');
    login.login_all(userList);
    #settings = tools.load_settings('settings_trainSoldiers.txt',8);
    para = tools.load_para('para_accelerate.txt');
    while(1):
        for i in range(0,userList['num']):
            #setting = settings[i];
            server = userList[str(i)]['server'];
            username = userList[str(i)]['username'];
            connection = userList[str(i)]['connection'];
            opener = connection['opener'];


            #timer= time.localtime();
            #print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
            #print 'Server :',server;
            #print 'User   :',username;


            #print time.time();
            citys = operation.get_citys(server,opener);
            for j in range(0,citys['num']):
                timer= time.localtime();
                print 'Time   :',str(timer.tm_hour)+':'+str(timer.tm_min)+':'+str(timer.tm_sec);
                print 'Server :',server;
                print 'User   :',username;
                print 'City  :',j;
                x = citys[str(j)]['x'];
                y = citys[str(j)]['y'];
                operation.switch(server,x,y,opener);
                #accelerate_once(server,para,opener);
            print '\n\n\n';
    return 0;