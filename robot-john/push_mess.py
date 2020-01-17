from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = "Wwdkx08Ttn19vpw/Um1MUUMQNERHoStXKNfJvJPCB0QchuiKmHfWBYrnPH/baNX11vtOPn3BFbOdd2KL3v98DlDj5ge5ca5WBo1rBy2hb+Km6iqjSyjC1ncAmWJuq6IwJp+AnM6TcovEGDVEKk3ChwdB04t89/1O/w1cDnyilFU="
to = "U3c9af44e12c2e955b48443f95424130e"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

#文字訊息

try:
    line_bot_api.push_message(to, TextSendMessage(text='台科大電腦研習社'))
except LineBotApiError as e:
    # error handle
    raise e