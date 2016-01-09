# coding=utf-8
import operation;
import string;
import time;
import login;
import tools;

time_delay_default = 100;
time_1000_second = 0.001;

def openBox_once(server,para,pkeys):
    city0 = operation.get_city0(server);
    resp = operation.get_transport_massages(server,city0['x'],city0['y']);
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
            resp = operation.open_box(server,5,1,pkeys);
            return resp.read();
        if (resource['nitu'] < para['ni']):
            print "Need NiTu";
            resp = operation.open_box(server,5,1,pkeys);
            return resp.read();
        if (resource['tiekuang'] < para['tie']):
            print "Need TieKuang";
            resp = operation.open_box(server,5,1,pkeys);
            return resp.read();
        if (resource['liangshi'] < para['liang']):
            print "Need LiangShi";
            resp = operation.open_box(server,5,1,pkeys);
            return resp.read();
    else:
        if (resource['mucai'] < para['mu_percent'] * resource['cangku'] / 100.0):
            print "Need MuCai";
            resp = operation.open_box(server,5,1,pkeys);
            return resp.read();
        if (resource['nitu'] < para['ni_percent'] * resource['cangku'] / 100.0):
            print "Need NiTu";
            resp = operation.open_box(server,5,1,pkeys);
            return resp.read();
        if (resource['tiekuang'] < para['tie_percent'] * resource['cangku'] / 100.0):
            print "Need TieKuang";
            resp = operation.open_box(server,5,1,pkeys);
            return resp.read();
        if (resource['liangshi'] < para['liang_percent'] * resource['liangcang'] / 100.0):
            print "Need LiangShi";
            resp = operation.open_box(server,5,1,pkeys);
            return resp.read();
    return "Satisfied";

def openBox(server,username,password,para):
    resp = login.login(username,password);
    while (1):
        while (login.check_login(server) != -1):
            resp = login.login(username, password);
            print resp.read();
            time.sleep(time_1000_second * time_delay_default);
        #para = transport.presetting0();
        pkeys = operation.get_openBox_pkeys(server);
        resp = openBox_once(server,para,pkeys);
        print resp;
        time.sleep(time_1000_second * time_delay_default);
    return;



settings = tools.load_para('settings_openBox.txt');
para = tools.load_paraString('user_openBox.txt');

openBox(para['server'],para['username'],para['password'],settings);
