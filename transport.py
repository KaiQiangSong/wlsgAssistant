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

transport_model_default = 0;
transport_model = transport_model_default;

def presetting0():
    para = {};
    para['model'] = 0;
    para['mu'] = 450000;
    para['ni'] = 450000;
    para['tie'] = 450000;
    para['liang'] = 450000;
    para['food_remain'] = 200000;
    return para;

def presetting1():
    para = [];
    para['model'] = 1;
    para['percent_cangku']= 80;
    para['percent_liangcang'] = 50;
    para['food_remain'] = 150000;
    return para;


def transport_needs(citys,para):
    citys_surplus = {};
    citys_surplus['num'] = citys['num'];
    for i in range(0,citys['num']):
        city = {};
        city['transport'] = (citys[str(i)]['shangren'] - citys[str(i)]['busy']) * citys[str(i)]['carry'];
        city['x'] = citys[str(i)]['x'];
        city['y'] = citys[str(i)]['y'];
        if (para['model'] == 1):
            if (i >0):
                city['mu'] = citys[str(i)]['mucai'] - citys[str(i)]['cangku'] * para['mu_percent'] / 100;
                city['ni'] = citys[str(i)]['nitu'] - citys[str(i)]['cangku'] * para['ni_percent'] / 100;
                city['tie'] = citys[str(i)]['tiekuang'] - citys[str(i)]['cangku'] * para['tie_percent'] / 100;
                city['liang'] = citys[str(i)]['liangshi'] - citys[str(i)]['cangku'] * para['liang_percent'] / 100;
            else:
                city['mu'] = citys[str(i)]['mucai']
                city['ni'] = citys[str(i)]['nitu']
                city['tie'] =  citys[str(i)]['tiekuang']
                city['liang'] = citys[str(i)]['liangshi'] - para['food_remain'];
        else:
            if (i > 0):
                city['mu'] = citys[str(i)]['mucai'] - para['mu'];
                city['ni'] = citys[str(i)]['nitu'] - para['ni'];
                city['tie'] =  citys[str(i)]['tiekuang'] - para['tie'];
                city['liang'] = citys[str(i)]['liangshi'] - para['liang'];
            else:
                city['mu'] = citys[str(i)]['mucai']
                city['ni'] = citys[str(i)]['nitu']
                city['tie'] =  citys[str(i)]['tiekuang']
                city['liang'] = citys[str(i)]['liangshi'] - para['food_remain'];
        citys_surplus[str(i)] = city;
        del city;
    return citys_surplus;


def transport_once(server,para,opener):
    #print time.time();
    citys = operation.get_citys(server,opener);
    #print time.time();
    citys = operation.get_resource(server,citys,opener);
    #print time.time();
    citys_surplus = transport_needs(citys,para);
    #print time.time();


    if (citys_surplus['0']['transport'] > 0):
        print 'Carry Ability: ',citys_surplus['0']['transport'];
        for i in range(1,citys_surplus['num']):
            mu = ni = tie = liang = 0;
            if (citys_surplus[str(i)]['mu'] < 0 and citys_surplus['0']['mu'] > 0):
                mu = min(0-citys_surplus[str(i)]['mu'],citys_surplus['0']['mu']);
            if (citys_surplus[str(i)]['ni'] < 0 and citys_surplus['0']['ni'] > 0):
                ni = min(0-citys_surplus[str(i)]['ni'],citys_surplus['0']['ni']);
            if (citys_surplus[str(i)]['tie'] < 0 and citys_surplus['0']['tie'] > 0):
                tie = min(0-citys_surplus[str(i)]['tie'],citys_surplus['0']['tie']);
            if (citys_surplus[str(i)]['liang'] < 0 and citys_surplus['0']['liang'] > 0):
                liang = min(0-citys_surplus[str(i)]['liang'],citys_surplus['0']['liang']);
            print 'City'+str(i)+' : ',mu,ni,tie,liang;
            total = mu + ni + tie + liang;
            if (total > 0):
                x1 = citys_surplus['0']['x'];
                y1 = citys_surplus['0']['y'];
                x2 = citys_surplus[str(i)]['x'];
                y2 = citys_surplus[str(i)]['y'];
                hour = 0;
                min1 = 0;
                if (total < citys_surplus['0']['transport']):
                    print 'Carry : ',mu,ni,tie,liang;
                    resp = operation.take_transport(server,x1,y1,x2,y2,mu,ni,tie,liang,hour,min1,opener);
                    return resp.read();
                else:
                    rate = citys_surplus['0']['transport'] * 1.0 / total;
                    mu = int(mu * rate);
                    ni = int(ni * rate);
                    tie = int(tie * rate);
                    liang = int(liang * rate);
                    print 'Carry : ',mu,ni,tie,liang;
                    resp = operation.take_transport(server,x1,y1,x2,y2,mu,ni,tie,liang,hour,min1,opener);
                    return resp.read();
        return "Satisfied";
    else:
        return "Busy";
    return "Error";

def transport_delay(server,username,password,para,opener,paraHTTP):
    retryTime = paraHTTP['retry_time'];
    while (retryTime > 0):
        flag = 0;
        try:
            resp = transport_once(server,para,opener);
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
            e = 'Socket Time Out';
            flag = 1;
        if (flag > 0):
            retryTime = retryTime - 1;
        else:
            break;
    # Forward the Exception Error
    if (flag):
        print error;
        return error;
    time.sleep(time_1000_second  *  para['time_delay']);
    return resp;

def main_program():
    userList = tools.load_user('user.txt');
    httpPara = tools.load_para('httpPara.txt');
    login.login_all(userList,httpPara);
    para_transport = tools.load_para('settings_transport.txt');
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
            #print time.time();
            resp = transport_delay(server,username,password,para_transport,opener,httpPara);
            #print time.time();
            print resp;
            print '\n\n\n';
    return 0;
