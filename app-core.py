from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
# Channel Access Token
line_bot_api = LineBotApi('hjHb8raZSh34EoQHWvHBrUtPU1JfXX7gVu6Y9oMeJ76Oklf3gilc7oFGGl4+0hoe54Gx4Ea4nV2Vw7fwdkEY3W1JZyzguJbr3kRjAZsvBA9ruwtEfBSlTJoukiHtVYJNaWsIQ+8ri7SIrZxlE4CAbwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('694dae22097e54525ff160df6662581c')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()
