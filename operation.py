# coding=utf-8
import urllib;
import urllib2;
import tools;
import time;
import string;
import cookielib;
import json;


def get_queue(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452073333621&act=get_queue&type=o&cache=false&r=1452073333729';
    return tools.get(url);

def set_city_resource(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452073333611&act=set_city_resource&type=o&cache=false&r=1452073333729';
    return tools.get(url);

def city_relationship(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_relationship&act=city_relationship&type=e&cache=false&r=1452076349230';
    return tools.get(url);

#NEED TO DO
def get_citys(server):
    content = city_relationship(server);
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

def get_money(server):
    url ='http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=_1452076349141&act=get_money&type=o&cache=false&r=1452076349231';
    return tools.get(url);


def city_profile(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_profile&act=city_profile&type=e&cache=false&r=1452076939722';
    return tools.get(url);


def city_build_resource(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php';
    para = {
        'ajaxId':'city_build_resource',
        'act':'city_build_resource',
        'type':'e',
        'cache':'false',
        'r':'1452077349870'
    };
    return tools.post(url,para);

def city_build_building(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_build_building&act=city_build_building&type=e&cache=false&r=1452077759249';
    return tools.get(url);

def polity_TuoHuangXinCheng(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=polity_TuoHuangXinCheng';
    para = {
        'ajaxId':'city_build_polity',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452078034879'
    };
    return tools.post(url,para);

def polity_QianDu(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=polity_QainDu';
    para = {
        'ajaxId':'city_build_QianDu',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452078759565'
    };
    return tools.post(url,para);

def city_trade_reassign(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_reassign&act=city_trade_reassign&type=e&cache=false&r=1452078884875';
    return tools.get(url);

def city_trade_transit(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_transit&act=city_trade_transit&type=e&cache=false&r=1452078978036';
    return tools.get(url);

def city_trade_buy(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=trade&ajaxId=city_trade_buy&act=city_trade_buy&type=e&cache=false&r=1452079029659';
    return tools.get(url);

def user_relation_0(server):
    url = 'http://'+server+'.sg.9wee.com/modules/user_relation.php?type=friend';
    para = {
        'ajaxId':'user_relation_0',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452079092783'
    };
    return tools.post(url,para);

def user_relation_1(server):
    url = 'http://'+server+'.sg.9wee.com/modules/user_relation.php?type=enemy';
    para = {
        'ajaxId':'user_relation_1',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452079234916'
    };
    return tools.post(url,para);

def city_manage_0(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_0&act=d&type=e&cache=false&r=1452079357777';
    return tools.get(url);

def city_manage_1(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_1&act=d&type=e&cache=false&r=1452079593042';
    return tools.get(url);

def city_manage_2(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_2&act=d&type=e&cache=false&r=1452079652585';
    return tools.get(url);

def city_manage_5(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_5&act=d&type=e&cache=false&r=1452079727777';
    return tools.get(url);

def city_manage_3(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_3&act=d&type=e&cache=false&r=1452079823091';
    return tools.get(url);

def city_manage_4(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=city_manage_4&act=d&type=e&cache=false&r=1452079864855';
    return tools.get(url);

def military_war_action(server):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_action.php';
    para = {
        'ajaxId':'military_war_action',
        'act':'military_war_action',
        'type':'e',
        'cache':'false',
        'r':'1452079973389'
    };
    return tools.post(url,para);

def military_war_news(server):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_news.php';
    para = {
        'ajaxId':'military_war_news',
        'act':'military_war_news',
        'type':'e',
        'cache':'false',
        'r':'1452080215593'
    };
    return tools.post(url,para);

def military_war_insurance(server):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_war_insurance.php';
    para = {
        'ajaxId':'military_war_insurance',
        'act':'military_war_insurance',
        'type':'e',
        'cache':'false',
        'r':'1452080641033'
    };
    return tools.post(url,para);

def military_general(server):
    url = 'http://'+server+'.sg.9wee.com/modules/military/military_general.php';
    para = {
        'ajaxId':'military_general',
        'act':'military_general',
        'type':'e',
        'cache':'false',
        'r':'1452081276675'
    }
    return tools.post(url,para);

def user_item(server):
    url = 'http://'+server+'.sg.9wee.com/modules/item/use_item.php?1452081445534';
    return tools.get(url);

def general_effect(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=item&ajaxId=general_effect&act=general_effect&type=e&cache=false&r=1452081446283';
    return tools.get(url);

def strengthen_item(server):
    url = 'http://wlh13.sg.9wee.com/modules/item/strengthen_item.php?1452081777741';
    return tools.get(url);

def embed_item(server):
    url = 'http://'+server+'.sg.9wee.com/modules/item/embed_item.php?1452082206327';
    return tools.get(url);

def repair_item(server):
    url = 'http://'+server+'.sg.9wee.com/modules/item/repair_item.php?1452082265693';
    return tools.get(url);

def lower_item(server):
    url = 'http://'+server+'.sg.9wee.com/modules/item/lower_item.php?1452082305357';
    return tools.get(url);

def hourse(server):
    url = 'http://'+server+'.sg.9wee.com/modules/horse/horse.php?ajaxId=military_general_zq&act=d&type=e&cache=false&request=horse_info&r=1452082349126';

def train_BuBing(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_BuBing';
    para = {
        'ajaxId':'soldier_train_1',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452082618070'
    };
    return tools.post(url,para);

def soldier(server):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?module=soldier&ajaxId=_1452082179073&act=get_city_army&type=o&cache=false&r=1452082626224';
    return tools.get(url);

def train_QiBing(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_QiBing';
    para = {
        'ajaxId':'soldier_train_2',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452082910625'
    };
    return tools.post(url,para);

def train_GoCheng(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_GongCheng';
    para = {
        'ajaxId':'soldier_train_3',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083129230'
    };
    return tools.post(url,para);

def train_TeShu(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_TeShu';
    para = {
        'ajaxId':'soldier_train_4',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083307202'
    };
    return tools.post(url,para);

def train_XianJing(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=train_XianJing';
    para = {
        'ajaxId':'soldier_train_5',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083577202',
    };
    return tools.post(url,para);

def research_WuQi(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=research_WuQi';
    para = {
        'ajaxId':'soldier_research_2',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083774824'
    };
    return tools.post(url,para);

def research_FangJu(server):
    url = 'http://'+server+'.sg.9wee.com/modules/train.php?action=show&type=research_FangJu';
    para = {
        'ajaxId':'soldier_research_3',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452083899287'
    };
    return tools.post(url,para);

def map_top(server):
    url = 'http://'+server+'.sg.9wee.com/modules/map.php';
    para = {
        'ajaxId':'map_top',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084142806'
    };
    return tools.post(url,para);

def map_show(server,x,y):
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
    return tools.post(url,para);

def union_yiguan(server):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_yiguan';
    para = {
        'ajaxId':'union_yiguan',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084640250'
    };
    return tools.post(url,para);

def union_lianmeng_gaikuang(server):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_gaikuang';
    para = {
        'ajaxId':'union_lianmeng_gaikuang',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084767653'
    };
    return tools.post(url,para);

def union_lianmeng_baoku(server):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_baoku';
    para = {
        'ajaxId':'union_baoku',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452084998025'
    };
    return tools.post(url,para);

def union_junqing(server):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_junqing';
    para = {
        'ajaxId':'union_junqing',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085288936'
    };
    return tools.post(url,para);

def union_lianmeng_shijian(server):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_lianmeng_shijian';
    para = {
        'ajaxId':'union_lianmeng_shijian',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085435933'
    };
    return tools.post(url,para);

def union_lianmeng_zhanbao(server,c1,c2):
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
    return tools.post(url,para);

def union_science(server):
    url = 'http://'+server+'.sg.9wee.com/modules/union.php?action=show&type=union_science';
    para = {
        'ajaxId':'union_science',
        'act':'d',
        'type':'e',
        'cache':'false',
        'r':'1452085832395'
    };
    return tools.post(url,para);

def switch(server,x,y):
    url = 'http://'+server+'.sg.9wee.com/switch.php?map_id='+str(x+400)+str(y+400);
    return tools.get(url);

def shop_time(server):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_time.php';
    para = {
        'ajaxId':'shop_time',
        'act':'shop_time',
        'type':'e',
        'cache':'false',
        'r':'1452086471119'
    };
    return tools.post(url,para);

def shop_general(server):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_general.php';
    para = {
        'ajaxId':'shop_general',
        'act':'shop_general',
        'type':'e',
        'cache':'false',
        'r':'1452086619541'
    };
    return tools.post(url,para);

def shop_box(server):
    url = 'http://'+server+'.sg.9wee.com/modules/military/shop_box.php';
    para = {
        'ajaxId':'shop_box',
        'act':'shop_box',
        'type':'e',
        'cache':'false',
        'r':'1452086804300'
    };
    return tools.post(url,para);

#transport

def get_transport_massages(server,x,y):
    url = 'http://'+server+'.sg.9wee.com/modules/gateway.php?ajaxId=ajax&act=d&type=e&cache=false&map='+str(x+400)+str(y+400)+'&time='+str(int(time.time()*1000));
    return tools.get(url);

def take_transport(server,x1,y1,x2,y2,mu,ni,tie,liang,hour,min):
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
    return tools.get(url);

