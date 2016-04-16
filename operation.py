# coding=utf-8
import urllib;
import urllib2;
import tools;
import time;
import string;
import cookielib;
import json;


def get_queue(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452073333621&act=get_queue&type=o&cache=false&r=1452073333729';
    return tools.get(url,opener,httpPara);

def set_city_resource(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452073333611&act=set_city_resource&type=o&cache=false&r=1452073333729';
    return tools.get(url,opener,httpPara);

def city_relationship(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_relationship&act=city_relationship&type=e&cache=false&r=1452076349230';
    return tools.get(url,opener,httpPara);

def get_citys(server,opener,httpPara):
    content = city_relationship(server,opener,httpPara);
    content = content.read();
    content = content.replace('<div class="new_city_no">','');
    content = content.replace('<ul>','');
    content = content.replace('<li><a href="/switch.php?map_id=','');
    content = content.replace('" onclick="','');
    content = content.replace("return switchCity('",' ');
    content = content.replace('\t',' ');
    content = content.replace("', '/switch.php?map_id=",' ');
    content = content.replace("');"+'">',' ');
    content = content.replace('</a></li>','');
    content = content.replace('</ul>','');
    content = content.replace('</div>','');
    #print content;
    content = content.split();
    num = len(content)/5;
    citys = {};
    citys['num'] = num;
    for i in range(0,num):
        citys[str(i)] = {
            'name' : content[ i * 5 + 1],
            'x' : string.atoi(content[i * 5]) / 1000 - 400,
            'y' : string.atoi(content[i * 5]) % 1000 - 400
        };
    return citys;

def get_city0(server,opener,httpPara):
    content = city_relationship(server,opener,httpPara);
    content = content.read();
    content = content.replace('<div class="new_city_no">','');
    content = content.replace('<ul>','');
    content = content.replace('<li><a href="/switch.php?map_id=','');
    content = content.replace('" onclick="','');
    content = content.replace("return switchCity('",' ');
    content = content.replace('\t',' ');
    content = content.replace("', '/switch.php?map_id=",' ');
    content = content.replace("');"+'">',' ');
    content = content.replace('</a></li>','');
    content = content.replace('</ul>','');
    content = content.replace('</div>','');
    #print content;
    content = content.split();
    num = len(content)/5;
    city0 = {
            'name' : content[1],
            'x' : string.atoi(content[0]) / 1000 - 400,
            'y' : string.atoi(content[0]) % 1000 - 400
    };
    return city0;

def get_money(server,opener,httpPara):
    url ='http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452076349141&act=get_money&type=o&cache=false&r=1452076349231';
    return tools.get(url,opener,httpPara);


def city_profile(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_profile&act=city_profile&type=e&cache=false&r=1452076939722';
    return tools.get(url,opener,httpPara);


def city_build_resource(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php';
    para = {
        'ajaxId':'city_build_resource',
        'act':'city_build_resource',
        'type':'e',
        'cache':'false',
        'r':'1452077349870'
    };
    return tools.post(url,para,opener,httpPara);

def city_build_building(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_build_building&act=city_build_building&type=e&cache=false&r=1452077759249';
    return tools.get(url,opener,httpPara);

def polity_TuoHuangXinCheng(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=polity_TuoHuangXinCheng';
    para = {
        'ajaxId':'city_build_polity',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452078034879'
    };
    return tools.post(url,para,opener,httpPara);

def polity_QianDu(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=polity_QainDu';
    para = {
        'ajaxId':'city_build_QianDu',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452078759565'
    };
    return tools.post(url,para,opener,httpPara);

def city_trade_reassign(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_reassign&act=city_trade_reassign&type=e&cache=false&r=1452078884875';
    return tools.get(url,opener,httpPara);

def city_trade_transit(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_transit&act=city_trade_transit&type=e&cache=false&r=1452078978036';
    return tools.get(url,opener,httpPara);

def city_trade_buy(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_buy&act=city_trade_buy&type=e&cache=false&r=1452079029659';
    return tools.get(url,opener,httpPara);

def user_relation_0(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/user_relation.php?type=friend';
    para = {
        'ajaxId':'user_relation_0',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452079092783'
    };
    return tools.post(url,para,opener,httpPara);

def user_relation_1(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/user_relation.php?type=enemy';
    para = {
        'ajaxId':'user_relation_1',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452079234916'
    };
    return tools.post(url,para,opener,httpPara);

def city_manage_0(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_0&act=d&type=e&cache=false&r=1452079357777';
    return tools.get(url,opener,httpPara);

def city_manage_1(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_1&act=d&type=e&cache=false&r=1452079593042';
    return tools.get(url,opener,httpPara);

def city_manage_2(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_2&act=d&type=e&cache=false&r=1452079652585';
    return tools.get(url,opener,httpPara);

def city_manage_5(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_5&act=d&type=e&cache=false&r=1452079727777';
    return tools.get(url,opener,httpPara);

def city_manage_3(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_3&act=d&type=e&cache=false&r=1452079823091';
    return tools.get(url,opener,httpPara);

def city_manage_4(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_4&act=d&type=e&cache=false&r=1452079864855';
    return tools.get(url,opener,httpPara);

def military_war_action(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_action.php';
    para = {
        'ajaxId':'military_war_action',
        'act':'military_war_action',
        'type':'e',
        'cache':'false',
        'r':'1452079973389'
    };
    return tools.post(url,para,opener,httpPara);

def military_war_news(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_news.php';
    para = {
        'ajaxId':'military_war_news',
        'act':'military_war_news',
        'type':'e',
        'cache':'false',
        'r':'1452080215593'
    };
    return tools.post(url,para,opener,httpPara);

def military_war_insurance(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_insurance.php';
    para = {
        'ajaxId':'military_war_insurance',
        'act':'military_war_insurance',
        'type':'e',
        'cache':'false',
        'r':'1452080641033'
    };
    return tools.post(url,para,opener,httpPara);

def military_general(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_general.php';
    para = {
        'ajaxId':'military_general',
        'act':'military_general',
        'type':'e',
        'cache':'false',
        'r':'1452081276675'
    }
    return tools.post(url,para,opener,httpPara);

def user_item(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/item/use_item.php?1452081445534';
    return tools.get(url,opener,httpPara);

def general_effect(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=item&ajaxId=general_effect&act=general_effect&type=e&cache=false&r=1452081446283';
    return tools.get(url,opener,httpPara);

def strengthen_item(server,opener,httpPara):
    url = 'http://wlh13.sg.9wee.com/modules/item/strengthen_item.php?1452081777741';
    return tools.get(url,opener,httpPara);

def embed_item(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/item/embed_item.php?1452082206327';
    return tools.get(url,opener,httpPara);

def repair_item(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/item/repair_item.php?1452082265693';
    return tools.get(url,opener,httpPara);

def lower_item(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/item/lower_item.php?1452082305357';
    return tools.get(url,opener,httpPara);

def hourse(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/horse/horse.php?ajaxId=military_general_zq&act=d&type=e&cache=false&request=horse_info&r=1452082349126';

def train_BuBing(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_BuBing';
    para = {
        'ajaxId':'soldier_train_1',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452082618070'
    };
    return tools.post(url,para,opener,httpPara);

def soldier(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=soldier&ajaxId=_1452082179073&act=get_city_army&type=o&cache=false&r=1452082626224';
    return tools.get(url,opener,httpPara);

def train_QiBing(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_QiBing';
    para = {
        'ajaxId':'soldier_train_2',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452082910625'
    };
    return tools.post(url,para,opener,httpPara);

def train_GongCheng(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_GongCheng';
    para = {
        'ajaxId':'soldier_train_3',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083129230'
    };
    return tools.post(url,para,opener,httpPara);

def train_TeShu(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_TeShu';
    para = {
        'ajaxId':'soldier_train_4',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083307202'
    };
    return tools.post(url,para,opener,httpPara);

def train_XianJing(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_XianJing';
    para = {
        'ajaxId':'soldier_train_5',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083577202',
    };
    return tools.post(url,para,opener,httpPara);

def research_WuQi(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=research_WuQi';
    para = {
        'ajaxId':'soldier_research_2',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083774824'
    };
    return tools.post(url,para,opener,httpPara);

def research_FangJu(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=research_FangJu';
    para = {
        'ajaxId':'soldier_research_3',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083899287'
    };
    return tools.post(url,para,opener,httpPara);

def map_top(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/map.php';
    para = {
        'ajaxId':'map_top',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084142806'
    };
    return tools.post(url,para,opener,httpPara);

def map_show(server,x,y,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/map.php?show';
    para = {
        'ajaxId':'',
        'act':'d',
        'type':'e',
        'cache':'false',
        'startX':-8+x,
        'startY':1+y,
        'r':'1452084427536'
    };
    return tools.post(url,para,opener,httpPara);

def union_yiguan(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_yiguan';
    para = {
        'ajaxId':'union_yiguan',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084640250'
    };
    return tools.post(url,para,opener,httpPara);

def union_lianmeng_gaikuang(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_gaikuang';
    para = {
        'ajaxId':'union_lianmeng_gaikuang',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084767653'
    };
    return tools.post(url,para,opener,httpPara);

def union_lianmeng_baoku(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_baoku';
    para = {
        'ajaxId':'union_baoku',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084998025'
    };
    return tools.post(url,para,opener,httpPara);

def union_junqing(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_junqing';
    para = {
        'ajaxId':'union_junqing',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085288936'
    };
    return tools.post(url,para,opener,httpPara);

def union_lianmeng_shijian(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_shijian';
    para = {
        'ajaxId':'union_lianmeng_shijian',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085435933'
    };
    return tools.post(url,para,opener,httpPara);

def union_lianmeng_zhanbao(server,c1,c2,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_zhanbao';
    para = {
        'ajaxId':'union_zhanbao',
        'act':'d',
        'type':'e',
        'cache':'false',
        'fortress_id':'',
        'c':'',
        'c1':c1,
        'c2':c2,
        'r':'1452085664881'
    };
    return tools.post(url,para,opener,httpPara);

def union_science(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_science';
    para = {
        'ajaxId':'union_science',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085832395'
    };
    return tools.post(url,para,opener,httpPara);

def switch(server,x,y,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/switch.php?map_id='+str(x+400)+str(y+400);
    return tools.get(url,opener,httpPara);

def shop_time(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_time.php';
    para = {
        'ajaxId':'shop_time',
        'act':'shop_time',
        'type':'e',
        'cache':'false',
        'r':'1452086471119'
    };
    return tools.post(url,para,opener,httpPara);

def shop_general(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_general.php';
    para = {
        'ajaxId':'shop_general',
        'act':'shop_general',
        'type':'e',
        'cache':'false',
        'r':'1452086619541'
    };
    return tools.post(url,para,opener,httpPara);

def shop_box(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_box.php';
    para = {
        'ajaxId':'shop_box',
        'act':'shop_box',
        'type':'e',
        'cache':'false',
        'r':'1452086804300'
    };
    return tools.post(url,para,opener,httpPara);

#transport

def get_transport_massages(server,x,y,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=ajax&act=d&type=e&cache=false&map='+str(x+400)+str(y+400)+'&time='+str(int(time.time()*1000));
    return tools.get(url,opener,httpPara);

def take_transport(server,x1,y1,x2,y2,mu,ni,tie,liang,hour,min,opener,httpPara):
    select1 = str(x1+400)+str(y1+400);
    select2 = str(x2+400)+str(y2+400);
    mu = str(mu);
    ni = str(ni);
    tie = str(tie);
    liang = str(liang);
    hour = str(hour);
    min = str(min);
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=yunshu&act=d&type=e&cache=false'+\
        '&mucai='+mu+\
        '&nitu='+ni+\
        '&select='+select1+\
        '&select2='+select2+\
        '&tiekuang='+tie+\
        '&hour1='+hour+\
        '&min1='+min+\
        '&liangshi='+liang+\
        '&hour2=&r=1452089051639';
    return tools.get(url,opener,httpPara);

def get_resource(server,citys,opener,httpPara):
    for i in range(0,citys['num']):
        resp = get_transport_massages(server,citys[str(i)]['x'],citys[str(i)]['y'],opener,httpPara);
        resp = resp.read();
        #print resp;
        resp = resp.replace(':',' ');
        resp = resp.replace('json=	{',' ');
        resp = resp.replace('}','');
        resp = resp.replace(',',' ');
        resp = resp.split();
        #print resp;
        num_attr = len(resp)/2;
        for j in range(2,num_attr):
            attr = resp[j*2];
            #print attr;
            #print citys[str(i)];
            citys[str(i)][attr] = string.atoi(resp[j*2+1]);
    return citys;

#open Box

def open_box(server,type,choice,pkeys,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_box.php';
    typeString = str(type+50);
    para = {
        'ajaxId':'_1452296694099',
        'act':'shop_box',
        'type':'e',
        'cache':'false',
        'choice':str(choice),
        'ptyle':'2',
        'pkey':pkeys[typeString],
        'pid': typeString,
        'action':'insert',
        'r':'1452297007844'
    };
    return tools.post(url,para,opener,httpPara);

def get_openBox_pkeys(server,opener,httpPara):
    resp = shop_box(server,opener,httpPara);
    resp = resp.read();
    pkeys = {};
    pos = resp.find("item_box_action(");
    while (pos != -1):
        end_pos = resp.find(',',pos+1);
        typeString = resp[pos+16:end_pos];
        pos1 = resp.find("'",end_pos+1)+1;
        pos2 = resp.find("'",pos1+1);
        pkey = resp[pos1:pos2];
        pkeys[typeString] = pkey;
        pos = resp.find("item_box_action(",pos+1);
    return pkeys;

#Train Soldiers

def train_soldiers(server,sid,number,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=do&type=train_JunDui';
    para = {
        'ajaxId':'',
        'act':'d',
        'type':'e',
        'cache':'false',
        'soldier_id':str(sid),
        'soldier_num':str(number),
        'r':'1452885050968'
    };
    return tools.post(url,para,opener,httpPara);

def train_show(server,sid,div_num,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_JunDui&confirm&soldier_id='\
        +str(sid)+'&div_num='+str(div_num);
    para = {
        'ajaxId':'_1452885960642',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452885960642'
    };
    return tools.post(url,para,opener,httpPara);

def get_train_limit(server,sid,div_num,opener,httpPara):
    resp = train_show(server,sid,div_num,opener,httpPara);
    resp = resp.read();
    pos1 = resp.find('本条队列最多可征募');
    str1 = resp[pos1+50:pos1+60];
    str1 = filter(str.isdigit,str1);
    pos2 = resp.find('总共可征募');
    str2 = resp[pos2+40:pos2+50];
    str2 =filter(str.isdigit,str2);
    if (str1 == ''):
        str1 = '0';
    if (str2 == ''):
        str2 = '0';
    #print str1,str2;
    resp = {
        'this' : string.atoi(str1),
        'all' : string.atoi(str2)
    }
    return resp;

# Accelerate
def get_accelerate_pkeys(server,opener,httpPara):
    resp = shop_time(server,opener,httpPara);
    resp = resp.read();
    pkeys = {};
    pos = resp.find("item_res_action(");
    while (pos != -1):
        end_pos = resp.find(',',pos+1);
        typeString = resp[pos+16:end_pos];
        pos1 = resp.find("'",end_pos+1)+1;
        pos2 = resp.find("'",pos1+1);
        pkey = resp[pos1:pos2];
        #print typeString,pkey;
        pkeys[typeString] = pkey;
        pos = resp.find("item_res_action(",pos+1);
    return pkeys;


def accelerate_military(server,pid,pkey,qid,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_time.php';
    para = {
        'ajaxId':'_1453190668809',
        'act':'shop_time',
        'type':'e',
        'cache':'false',
        'ptyle':'2',
        'sid':'',
        'pkey':pkey,
        'pid':str(pid),
        'qid':str(qid),
        'action':'insert',
        'r':'1453190676115'
    };
    return tools.post(url,para,opener,httpPara);

def accelerate_research(server,pid,pkey,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_time.php';
    para = {
        'ajaxId':'_1458955253380',
        'act':'shop_time',
        'type':'e',
        'cache':'false',
        'ptyle':'2',
        'sid':'',
        'pkey':pkey,
        'pid':pid,
        'action':'insert',
        'r':'1458955295179'
    };
    return tools.post(url,para,opener,httpPara);

def get_queue_num_BuBing(server,opener,httpPara):
    resp = train_BuBing(server,opener,httpPara).read();
    pos1 = resp.find('[队列数：');
    if (pos1 == -1):
        return 0;
    pos2 = resp.find('/',pos1+1);
    return string.atoi(resp[pos2-1:pos2]);

def get_queue_num_QiBing(server,opener,httpPara):
    resp = train_QiBing(server,opener,httpPara).read();
    pos1 = resp.find('[队列数：');
    if (pos1 == -1):
        return 0;
    pos2 = resp.find('/',pos1+1);
    return string.atoi(resp[pos2-1:pos2]);

def get_queue_num_GongCheng(server,opener,httpPara):
    resp = train_GongCheng(server,opener,httpPara).read();
    pos1 = resp.find('[队列数：');
    if (pos1 == -1):
        return 0;
    pos2 = resp.find('/',pos1+1);
    return string.atoi(resp[pos2-1:pos2]);

def get_queue_num_TeShu(server,opener,httpPara):
    resp = train_TeShu(server,opener,httpPara).read();
    pos1 = resp.find('[队列数：');
    if (pos1 == -1):
        return 0;
    pos2 = resp.find('/',pos1+1);
    return string.atoi(resp[pos2-1:pos2]);

#Build

def shop(server,queue_id,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop.php';
    para = {
        'ajaxId':'_1453185831404',
        'act':'shopcom',
        'type':'e',
        'cache':'false',
        'action':'build_time_add',
        'queue_id':queue_id,
        'r':'1453185841059'
    };
    return tools.post(url,para,opener,httpPara);

def get_build_sids(server,queue_id,opener,httpPara):
    resp = shop(server,queue_id,opener,httpPara);
    resp = resp.read();
    sids = {};
    if (resp.find('<div class="fl"'+" id='military_build' style='display:block'>") != -1):
        sids['model'] = 1;
    else:
        sids['model'] = 0;
    pos = resp.find("id='item_value'"+' type="radio" value=');
    while (pos != -1):
        pos1 = resp.find(":",pos+1);
        typeString = resp[pos+36:pos1];
        pos2 = resp.find("'",pos1+1);
        sid = resp[pos+36:pos2];
        sids[typeString] = sid;
        #print typeString,sid;
        pos = resp.find("id='item_value'"+' type="radio" value=',pos+1);
    return sids;

def demolish_building(server,pid,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=cc&act=demolish_building&type=o&cache=false&pid='+str(pid)+'&r=1453215883283'
    return tools.get(url,opener,httpPara);

def upgrade_building(server,pid,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=sj&act=upgrade_building&type=o&cache=false&pid='+str(pid)+'&r=1453216112315';
    return tools.get(url,opener,httpPara);

def get_building_levels(server,opener,httpPara):
    levels = {};

    resp = city_build_resource(server,opener,httpPara);
    resp = resp.read();
    pos = resp.find("mask.loadInfo('/modules/build/build.php?rid=");
    while (pos != -1):
        pos1 = pos + 44;
        pos2 = resp.find("'",pos1);
        pid = resp[pos1:pos2];
        pos1 = resp.find('<div class="sg_jza_lv">',pos2) + 23;
        pos2 = resp.find('<',pos1);
        level = string.atoi(resp[pos1:pos2]);
        pos = resp.find("mask.loadInfo('/modules/build/build.php?rid=",pos2);
        if (pos < 0):
            break;
        pos1 = pos + 44;
        pos2 = resp.find("'",pos1);
        pid2 = resp[pos1:pos2];
        while (pid == pid2):
            pos = resp.find("mask.loadInfo('/modules/build/build.php?rid=",pos2);
            pos1 = pos + 44;
            pos2 = resp.find("'",pos1);
            pid2 = resp[pos1:pos2];
        if (pid not in levels):
            levels[pid] = level;
        else:
            print 'Repeat';
        #print pid,level;

    resp = city_build_building(server,opener,httpPara);
    resp = resp.read();
    pos = resp.find('<a href="#" onclick="'+"mask.loadInfo('/modules/build/build.php?rid=");
    while (pos != -1):
        pos1 = pos + 65;
        pos2 = resp.find("'",pos1);
        pid = resp[pos1:pos2];
        pos1 = resp.find('<div class="sg_jza_lv">',pos2) + 23;
        pos2 = resp.find('<',pos1);
        level = string.atoi(resp[pos1:pos2]);
        pos = resp.find('<a href="#" onclick="'+"mask.loadInfo('/modules/build/build.php?rid=",pos2);
        #pos = resp.find('<a href="#" onclick="'+"mask.loadInfo('/modules/build/build.php?rid=",pos+1);
        levels[pid] = level;
    return levels;

def get_building_information(server,opener,httpPara):
    resp = get_queue(server,opener,httpPara);
    message = json.load(resp);
    if (message[1]['is_building'] == None):
        return "无在建建筑";
    else:
        return message[1]['is_building'][0];

def accelerate_building(server,queue_id,sid,opener,httpPara):
    url = 'http://wlh13.sg.9wee.com/modules/military/shop_time.php';
    para = {
        'ajaxId':'_1453228315005',
        'act':'shop_time',
        'type':'e',
        'cache':'false',
        'ptyle':'2',
        'sid':sid,
        'queue_id':queue_id,
        'pid':'',
        'pkey':'',
        'action':'insert',
        'r':'1453228321209'
    };
    return tools.post(url,para,opener,httpPara);

#Reserach

def research_WuQi(server,soliderId,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=do&type=research_WuQi';
    para = {
        'ajaxId':'',
        'act':'d',
        'type':'e',
        'cache':'false',
        'soldier_id':str(soliderId),
        'r':'1453531501235'
    };
    return tools.post(url,para,opener,httpPara);

def research_FangJu(server,soliderId,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=do&type=research_FangJu';
    para = {
        'ajaxId':'',
        'act':'d',
        'type':'e',
        'cache':'false',
        'soldier_id':str(soliderId),
        'r':'1453532829170'
    };
    return tools.post(url,para,opener,httpPara);

def research_BingZhong(server,soliderId,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=do&type=research_BingZhong';
    para = {
        'ajaxId':'',
        'act':'d',
        'type':'e',
        'cache':'false',
        'soldier_id':str(soliderId),
        'r':'1453532995761'
    };
    return tools.post(url,para,opener,httpPara);

# Activate Buffs
def activate_general_buffs(server,pid,pkey,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_general.php';
    para = {
        'ajaxId':'_1458499690182',
        'act':'shop_general',
        'type':'e',
        'cache':'false',
        'ptyle':'2',
        'pkey':pkey,
        'pid': pid,
        'action':'insert',
        'r':'1458499923285'
    };
    return tools.post(url,para,opener,httpPara);

def shop_general(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_general.php';
    para = {
        'ajaxId':'shop_general',
        'act':'shop_general',
        'type':'e',
        'cache':'false',
        'r':'1458499698496'
    };
    return tools.post(url,para,opener,httpPara);

def get_general_pkeys(server,opener,httpPara):
    resp = shop_general(server,opener,httpPara);
    resp = resp.read();
    pkeys = {};
    pos = resp.find("item_res_action(");
    while (pos != -1):
        pos1 = resp.find('(',pos+1);
        pos2 = resp.find(',',pos+1);
        pos3 = resp.find(')',pos2+1);
        typeString = resp[pos1+1:pos2];
        typeString = typeString.strip("'");
        pkey = resp[pos2+1:pos3];
        pkey = pkey.strip("'");
        #print typeString,':',pkey;
        pkeys[typeString] = pkey;
        pos = resp.find("item_res_action(",pos3+1);
    return pkeys;

def change_Soldiers(server,sid,num,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/soldier_change.php';
    para = {
        'ajaxId':'_1459063807623',
        'act':'d',
        'type':'e',
        'cache':'false',
        'action':'change',
        'change_type_id':'1',
        'soldiers_id':sid,
        'soldiers_num':num,
        'r':'1459063814107'
    };
    return tools.post(url,para,opener,httpPara);

def show_change_Soldiers(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/military/soldier_change.php?action=show';
    para = {
        'ajaxId':'_1459066175043',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1459066175043'
    };
    return tools.post(url,para,opener,httpPara);

def get_change_Soldiers(server,opener,httpPara):
    resp = show_change_Soldiers(server,opener,httpPara).read();
    soldiers = {};
    pos = resp.find('<input type="hidden" name="');
    while (pos!=-1):
        pos1 = resp.find('value="',pos+1);
        pos2 = resp.find('/>',pos1+1);
        s1 = resp[pos+38:pos1-2];
        s2 = resp[pos1+7:pos2-1];
        soldiers[s1] = string.atoi(s2);
        #print s1;
        #print s2;
        pos = resp.find('<input type="hidden" name="',pos2+1);
    return soldiers;


def activate_vip(server,vipType,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/vip.php';
    para = {
        'ajaxId':'_1460753029498',
        'act':'d',
        'type':'e',
        'cache':'false',
        'action':'d',
        'request':'exchange',
        'vip_type':vipType,
        'r':'1460753069764'
    };
    return tools.post(url,para,opener,httpPara);

def check_vip(server,opener,httpPara):
    url = 'http://'+server+'.sg.9wee.com/modules/vip.php';
    para = {
        'ajaxId':'_1460753035655',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1460753035656'
    };
    return tools.post(url,para,opener,httpPara);

def get_vip_info(server,opener,httpPara):
    resp = check_vip(server,opener,httpPara);
    resp = resp.read();
    pos = resp.find('当前身份');
    pos1 = resp.find('<div class="sg_lm_m_c">',pos);
    pos2 = resp.find('</div>',pos1);
    str1 = resp[pos1+23:pos2];
    info = {};
    info['vType'] = -1;
    if (str1.find('普通用户') != -1):
        info['vType'] = 0;
    if (str1.find('白金VIP') != -1):
        info['vType'] = 136;
    if (str1.find('钻石VIP') != -1):
        info['vType'] = 137;
    if (info['vType'] > 0):
        pos1 = str1.find('：');
        pos2 = str1.find('-');
        tstr = str1[pos1+3:pos2];
        info['year'] = string.atoi(tstr);
        pos3 = str1.find('-',pos2+1);
        tstr = str1[pos2+1:pos3];
        info['month'] = string.atoi(tstr);
        pos4 = str1.find(' ',pos3+1);
        tstr = str1[pos3+1:pos4];
        info['day'] = string.atoi(tstr);
        pos5 = str1.find(':',pos4+1);
        tstr = str1[pos4+1:pos5];
        info['hour'] = string.atoi(tstr);
        pos6 = str1.find(':',pos5+1);
        tstr = str1[pos5+1:pos6];
        info['minute'] = string.atoi(tstr);
        pos7 = str1.find(')',pos6+1);
        tstr = str1[pos6+1:pos7];
        info['second'] = string.atoi(tstr);
    return info;
