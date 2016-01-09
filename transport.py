# coding=utf-8
import operation;
import string;
import time;
import login;

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
        if (transport_model):
            resource_need = citys[str(i)]['cangku'] * para['percent_cangku'] / 100;
            food_need = citys[str(i)]['liangcang'] * para['percent_liangcang'] / 100;
            if (not i):
                resource_need = 0;
                food_need = para['food_remain'];
            city['mu'] = citys[str(i)]['mucai'] - resource_need;
            city['ni'] = citys[str(i)]['nitu'] - resource_need;
            city['tie'] = citys[str(i)]['tie'] - resource_need;
            city['liang'] = citys[str(i)]['liang'] - food_need;
        else:
            if (i):
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

def transport_once(server,para):
    #print time.time();
    citys = operation.get_citys(server);
    #print time.time();
    citys = operation.get_resource(server,citys);
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
                    resp = operation.take_transport(server,x1,y1,x2,y2,mu,ni,tie,liang,hour,min1);
                    return resp.read();
                else:
                    rate = citys_surplus['0']['transport'] * 1.0 / total;
                    mu = int(mu * rate);
                    ni = int(ni * rate);
                    tie = int(tie * rate);
                    liang = int(liang * rate);
                    print 'Carry : ',mu,ni,tie,liang;
                    resp = operation.take_transport(server,x1,y1,x2,y2,mu,ni,tie,liang,hour,min1);
                    return resp.read();
        return "Satisfied";
    else:
        return "Busy";
    return "Error";

def transport_all(server,username,password,para):
    resp = login.login(username,password);

    while (login.check_login(server) != -1):
        resp = login.login(username, password);
        print resp.read();
        time.sleep(0.1);
    #para = transport.presetting0();
    resp = transport_once(server,para);
    print resp;
    time.sleep(0.1);
    return;