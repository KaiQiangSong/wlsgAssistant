# coding=utf-8
import login;
import operation;
import time;
import string;

time_delay_default = 100;
time_1000_second = 0.001;

username = u'弑魂25';
password = 'tianxing';
server = 'wlh13';

resp = login.login(username, password);
print resp.read();

resp = login.get_main(server);
print resp.read();

resp = login.check_login(server);
print resp;

while (login.check_login(server) != -1):
    resp = login.login(username, password);
    time.sleep(time_1000_second * time_delay_default);

content = operation.city_relationship(server);
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
print content;
content = content.split();
print len(content);
print content;

num = len(content)/5;
citys = {};
citys['num'] = num;
for i in range(num):
    citys[str(i)] = {
        'name' : content[ i * 5 -2],
        'x' : (string.atoi(content[i * 5 - 3]) / 1000) - 400,
        'y' : (string.atoi(content[i * 5 - 3]) % 1000) - 400
    };
print citys;
