from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

import requests, hashlib, time, os
from bs4 import BeautifulSoup

CHANNEL_ACCESS_TOKEN = "Wwdkx08Ttn19vpw/Um1MUUMQNERHoStXKNfJvJPCB0QchuiKmHfWBYrnPH/baNX11vtOPn3BFbOdd2KL3v98DlDj5ge5ca5WBo1rBy2hb+Km6iqjSyjC1ncAmWJuq6IwJp+AnM6TcovEGDVEKk3ChwdB04t89/1O/w1cDnyilFU="
john = "U3c9af44e12c2e955b48443f95424130e"
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

# =================================================================
#line_bot_api.push_message(john, TextSendMessage(text = "Program Start!!"))
# =================================================================

unit = 300
cur_time = int(time.time() + 28800)
hour_pre = cur_time - (cur_time % unit)

def update():
    data = []
    url = 'http://coolpc.com.tw/phpBB2/portal.php'
    html = requests.get(url).text.encode('utf-8-sig')
    sp = BeautifulSoup(html, 'html.parser')
    class_cat = sp.find('td', {'class':'cat'})
    new_link = 'http://coolpc.com.tw/phpBB2' + class_cat.find_all('a')[1].get('href').lstrip('.')
    strong = class_cat.find('strong').text
    md5 = hashlib.md5(class_cat.text.encode('utf-8-sig')).hexdigest()
    data.append(md5)
    data.append(new_link)
    data.append(strong)
    return data

cur_md5 = pre_md5 = ''

while True:
    cur_time = int(time.time() + 28800)
    hour_cur = cur_time - (cur_time % unit)
    hm_time = time.strftime("%H:%M", time.gmtime(hour_cur))
    
    if hour_cur != hour_pre:
        hour_pre = hour_cur
        data = update()
        cur_md5 = data[0]
        with open('pre_md5.txt', 'r') as f:
            pre_md5 = f.read()
        if cur_md5 != pre_md5:            
            with open('pre_md5.txt', 'w') as f:
                f.write(cur_md5)
            try:
                line_bot_api.push_message(john, TextSendMessage(text = data[2]))
                line_bot_api.push_message(john, TextSendMessage(text = data[1]))
            except LineBotApiError as e:
                # error handle
                raise e