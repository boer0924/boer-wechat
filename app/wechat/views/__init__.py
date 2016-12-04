# -*- coding: utf-8 -*-

from hashlib import sha1
# import urllib2
# import json
import requests

from flask import current_app, request, make_response
# from app.wechat import wechat
from .. import wechat
from ..utils.message import msg_recv, msg_send

@wechat.route('/token')
def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + current_app.config['APPID'] + '&secret=' + current_app.config['APPSECRET']
    # resp = urllib2.urlopen(url).read()
    # access_token = json.loads(resp).get('access_token', '40013')
    access_token = requests.get(url).json().get('access_token', '40013')
    return access_token

@wechat.route('/create/menu')
def create():
    access_token = get_access_token()
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + access_token
    menu = {
        "button":[
            {	
                "type":"click",
                "name":"今日歌曲",
                "key":"V1001_TODAY_MUSIC"
            },
            {
                "name":"菜单",
                "sub_button":[
                    {	
                        "type":"view",
                        "name":"搜索",
                        "url":"http://www.soso.com/"
                    },
                    {
                        "type":"view",
                        "name":"视频",
                        "url":"http://v.qq.com/"
                    },
                    {
                    "type":"click",
                    "name":"赞一下我们",
                    "key":"V1001_GOOD"
                    }
                ]
            }
        ]
    }

    resp = requests.post(url, data=menu)
    return resp.text

@wechat.route('/', methods=['GET', 'POST'])
def check_signature():
    # return 'Hello WeChat'
    # signature = request.args.get('signature')
    # timestamp = request.args.get('timestamp')
    # nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')

    # token = current_app.config['TOKEN']

    # tmplist = [token, signature, nonce]
    # tmplist.sort()
    # tmpstr = ''.join(tmplist)
    # if sha1(tmpstr).hexdigest() == signature:
    #     return True
    # else:
    #     return False
    if request.method == 'POST':
        user_msg = msg_recv(request.data)
        reply = msg_send(user_msg)
        resp = make_response(reply)
        resp.content_type = 'application/xml'
        return resp
    return echostr