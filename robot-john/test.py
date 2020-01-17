from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = "Wwdkx08Ttn19vpw/Um1MUUMQNERHoStXKNfJvJPCB0QchuiKmHfWBYrnPH/baNX11vtOPn3BFbOdd2KL3v98DlDj5ge5ca5WBo1rBy2hb+Km6iqjSyjC1ncAmWJuq6IwJp+AnM6TcovEGDVEKk3ChwdB04t89/1O/w1cDnyilFU="
john = "U3c9af44e12c2e955b48443f95424130e"
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

import time

unit = 60
cur_time = int(time.time() + 28800)
hour_pre = cur_time - (cur_time % unit)

while True:
    cur_time = int(time.time() + 28800)
    hour_cur = cur_time - (cur_time % unit)
    if hour_cur != hour_pre:
        hour_pre = hour_cur
        line_bot_api.push_message(john, TextSendMessage(text = "Program Start!!"))
