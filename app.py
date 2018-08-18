# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('oo4wjX+TAf9pQUxpCTxYT1OfENwpYUxqDjgTOF5QncJaQ07tiZYqT/Ydb+0+LYfK3h5BwleD5k5kl8liYBgruEWZQR2n1zXzfvXHoLEF17Gv/ofasR39HAbLso8kUyrZg0NNbdw1rDLdD0VnJF8fogdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7e50c9e6ff0b711135328a6623b90328')



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

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)