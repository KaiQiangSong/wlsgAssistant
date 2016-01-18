# coding=utf-8
import urllib;
import urllib2;
import tools;
import time;
import string;
import cookielib;
import json;


def get_queue(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452073333621&act=get_queue&type=o&cache=false&r=1452073333729';
    return tools.get(url,opener);

def set_city_resource(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452073333611&act=set_city_resource&type=o&cache=false&r=1452073333729';
    return tools.get(url,opener);

def city_relationship(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_relationship&act=city_relationship&type=e&cache=false&r=1452076349230';
    return tools.get(url,opener);

def get_citys(server,opener):
    content = city_relationship(server,opener);
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

def get_city0(server,opener):
    content = city_relationship(server,opener);
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

def get_money(server,opener):
    url ='http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452076349141&act=get_money&type=o&cache=false&r=1452076349231';
    return tools.get(url,opener);


def city_profile(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_profile&act=city_profile&type=e&cache=false&r=1452076939722';
    return tools.get(url,opener);


def city_build_resource(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php';
    para = {
        'ajaxId':'city_build_resource',
        'act':'city_build_resource',
        'type':'e',
        'cache':'false',
        'r':'1452077349870'
    };
    return tools.post(url,para,opener);

def city_build_building(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_build_building&act=city_build_building&type=e&cache=false&r=1452077759249';
    return tools.get(url,opener);

def polity_TuoHuangXinCheng(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=polity_TuoHuangXinCheng';
    para = {
        'ajaxId':'city_build_polity',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452078034879'
    };
    return tools.post(url,para,opener);

def polity_QianDu(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=polity_QainDu';
    para = {
        'ajaxId':'city_build_QianDu',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452078759565'
    };
    return tools.post(url,para,opener);

def city_trade_reassign(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_reassign&act=city_trade_reassign&type=e&cache=false&r=1452078884875';
    return tools.get(url,opener);

def city_trade_transit(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_transit&act=city_trade_transit&type=e&cache=false&r=1452078978036';
    return tools.get(url,opener);

def city_trade_buy(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_buy&act=city_trade_buy&type=e&cache=false&r=1452079029659';
    return tools.get(url,opener);

def user_relation_0(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/user_relation.php?type=friend';
    para = {
        'ajaxId':'user_relation_0',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452079092783'
    };
    return tools.post(url,para,opener);

def user_relation_1(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/user_relation.php?type=enemy';
    para = {
        'ajaxId':'user_relation_1',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452079234916'
    };
    return tools.post(url,para,opener);

def city_manage_0(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_0&act=d&type=e&cache=false&r=1452079357777';
    return tools.get(url,opener);

def city_manage_1(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_1&act=d&type=e&cache=false&r=1452079593042';
    return tools.get(url,opener);

def city_manage_2(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_2&act=d&type=e&cache=false&r=1452079652585';
    return tools.get(url,opener);

def city_manage_5(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_5&act=d&type=e&cache=false&r=1452079727777';
    return tools.get(url,opener);

def city_manage_3(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_3&act=d&type=e&cache=false&r=1452079823091';
    return tools.get(url,opener);

def city_manage_4(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_4&act=d&type=e&cache=false&r=1452079864855';
    return tools.get(url,opener);

def military_war_action(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_action.php';
    para = {
        'ajaxId':'military_war_action',
        'act':'military_war_action',
        'type':'e',
        'cache':'false',
        'r':'1452079973389'
    };
    return tools.post(url,para,opener);

def military_war_news(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_news.php';
    para = {
        'ajaxId':'military_war_news',
        'act':'military_war_news',
        'type':'e',
        'cache':'false',
        'r':'1452080215593'
    };
    return tools.post(url,para,opener);

def military_war_insurance(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_insurance.php';
    para = {
        'ajaxId':'military_war_insurance',
        'act':'military_war_insurance',
        'type':'e',
        'cache':'false',
        'r':'1452080641033'
    };
    return tools.post(url,para,opener);

def military_general(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_general.php';
    para = {
        'ajaxId':'military_general',
        'act':'military_general',
        'type':'e',
        'cache':'false',
        'r':'1452081276675'
    }
    return tools.post(url,para,opener);

def user_item(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/item/use_item.php?1452081445534';
    return tools.get(url,opener);

def general_effect(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=item&ajaxId=general_effect&act=general_effect&type=e&cache=false&r=1452081446283';
    return tools.get(url,opener);

def strengthen_item(server,opener):
    url = 'http://wlh13.sg.9wee.com/modules/item/strengthen_item.php?1452081777741';
    return tools.get(url,opener);

def embed_item(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/item/embed_item.php?1452082206327';
    return tools.get(url,opener);

def repair_item(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/item/repair_item.php?1452082265693';
    return tools.get(url,opener);

def lower_item(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/item/lower_item.php?1452082305357';
    return tools.get(url,opener);

def hourse(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/horse/horse.php?ajaxId=military_general_zq&act=d&type=e&cache=false&request=horse_info&r=1452082349126';

def train_BuBing(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_BuBing';
    para = {
        'ajaxId':'soldier_train_1',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452082618070'
    };
    return tools.post(url,para,opener);

def soldier(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=soldier&ajaxId=_1452082179073&act=get_city_army&type=o&cache=false&r=1452082626224';
    return tools.get(url,opener);

def train_QiBing(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_QiBing';
    para = {
        'ajaxId':'soldier_train_2',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452082910625'
    };
    return tools.post(url,para,opener);

def train_GoCheng(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_GongCheng';
    para = {
        'ajaxId':'soldier_train_3',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083129230'
    };
    return tools.post(url,para,opener);

def train_TeShu(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_TeShu';
    para = {
        'ajaxId':'soldier_train_4',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083307202'
    };
    return tools.post(url,para,opener);

def train_XianJing(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_XianJing';
    para = {
        'ajaxId':'soldier_train_5',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083577202',
    };
    return tools.post(url,para,opener);

def research_WuQi(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=research_WuQi';
    para = {
        'ajaxId':'soldier_research_2',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083774824'
    };
    return tools.post(url,para,opener);

def research_FangJu(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=research_FangJu';
    para = {
        'ajaxId':'soldier_research_3',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083899287'
    };
    return tools.post(url,para,opener);

def map_top(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/map.php';
    para = {
        'ajaxId':'map_top',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084142806'
    };
    return tools.post(url,para,opener);

def map_show(server,x,y,opener):
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
    return tools.post(url,para,opener);

def union_yiguan(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_yiguan';
    para = {
        'ajaxId':'union_yiguan',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084640250'
    };
    return tools.post(url,para,opener);

def union_lianmeng_gaikuang(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_gaikuang';
    para = {
        'ajaxId':'union_lianmeng_gaikuang',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084767653'
    };
    return tools.post(url,para,opener);

def union_lianmeng_baoku(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_baoku';
    para = {
        'ajaxId':'union_baoku',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084998025'
    };
    return tools.post(url,para,opener);

def union_junqing(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_junqing';
    para = {
        'ajaxId':'union_junqing',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085288936'
    };
    return tools.post(url,para,opener);

def union_lianmeng_shijian(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_shijian';
    para = {
        'ajaxId':'union_lianmeng_shijian',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085435933'
    };
    return tools.post(url,para,opener);

def union_lianmeng_zhanbao(server,c1,c2,opener):
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
    return tools.post(url,para,opener);

def union_science(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_science';
    para = {
        'ajaxId':'union_science',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085832395'
    };
    return tools.post(url,para,opener);

def switch(server,x,y,opener):
    url = 'http://'+server+'.sg.9wee.com/switch.php?map_id='+str(x+400)+str(y+400);
    return tools.get(url,opener);

def shop_time(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_time.php';
    para = {
        'ajaxId':'shop_time',
        'act':'shop_time',
        'type':'e',
        'cache':'false',
        'r':'1452086471119'
    };
    return tools.post(url,para,opener);

def shop_general(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_general.php';
    para = {
        'ajaxId':'shop_general',
        'act':'shop_general',
        'type':'e',
        'cache':'false',
        'r':'1452086619541'
    };
    return tools.post(url,para,opener);

def shop_box(server,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_box.php';
    para = {
        'ajaxId':'shop_box',
        'act':'shop_box',
        'type':'e',
        'cache':'false',
        'r':'1452086804300'
    };
    return tools.post(url,para,opener);

#transport

def get_transport_massages(server,x,y,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=ajax&act=d&type=e&cache=false&map='+str(x+400)+str(y+400)+'&time='+str(int(time.time()*1000));
    return tools.get(url,opener);

def take_transport(server,x1,y1,x2,y2,mu,ni,tie,liang,hour,min,opener):
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
    return tools.get(url,opener);

def get_resource(server,citys,opener):
    for i in range(0,citys['num']):
        resp = get_transport_massages(server,citys[str(i)]['x'],citys[str(i)]['y'],opener);
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

def open_box(server,type,choice,pkeys,opener):
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
    return tools.post(url,para,opener);

def get_openBox_pkeys(server,opener):
    resp = shop_box(server,opener);
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

def train_soldiers(server,sid,number,opener):
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
    return tools.post(url,para,opener);

def train_show(server,sid,div_num,opener):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_JunDui&confirm&soldier_id='\
        +str(sid)+'&div_num='+str(div_num);
    para = {
        'ajaxId':'_1452885960642',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452885960642'
    };
    return tools.post(url,para,opener);

def get_train_limit(server,sid,div_num,opener):
    resp = train_show(server,sid,div_num,opener);
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