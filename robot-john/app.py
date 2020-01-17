import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import pandas as pd
import datetime
import numpy as np

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    'Wwdkx08Ttn19vpw/Um1MUUMQNERHoStXKNfJvJPCB0QchuiKmHfWBYrnPH/baNX11vtOPn3BFbOdd2KL3v98DlDj5ge5ca5WBo1rBy2hb+Km6iqjSyjC1ncAmWJuq6IwJp+AnM6TcovEGDVEKk3ChwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('571366145dc02bf0639938750e7f2823')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return ' OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #receive = event.message.text
    # png_path = 'https://drv.tw/~90618143@gcloud.csu.edu.tw/gd/stock_image/'
    # message = ImageSendMessage(
    #    original_content_url=png_path + receive + '.png',
    #    preview_image_url=png_path + receive + '.png'
    #)
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text = event.message.text))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
