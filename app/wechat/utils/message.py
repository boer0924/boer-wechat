# -*- coding: utf-8 -*-

'WeChat message tools package'

import xml.etree.ElementTree as ET
import time

def msg_recv(data):
    tree = ET.fromstring(data)
    tousername = tree.find('ToUserName').text
    fromusername = tree.find('FromUserName').text
    createtime = tree.find('CreateTime').text
    msgtype = tree.find('MsgType').text
    if msgtype == 'event':
        event = tree.find('Event').text
        if event == 'subscribe':
            pass
        return dict(
            tousername = tousername,
            fromusername = fromusername,
            createtime = createtime,
            msgtype = msgtype,
            event = event
        )
    else:
        content = tree.find('Content').text
        msgid = tree.find('MsgId').text
        return dict(
            tousername = tousername,
            fromusername = fromusername,
            createtime = createtime,
            msgtype = msgtype,
            content = content,
            msgid = msgid
        )

def msg_send(data):
    tousername = data.get('fromusername')
    fromusername = data.get('tousername')
    createtime = int(time.time())
    msgtype = data.get('msgtype')
    if msgtype == 'event':
        event = data.get('event')
        if event == 'subscribe':
            content = '''
欢迎关注《海之博·纳百川》
回复python: 获取更多Python相关信息
回复linux: 获取更多Linux相关信息
回复awesome: 获取更多劲爆信息...
            '''
    else:
        if data.get('content').lower() == 'python':
            content = 'Hello Python'
        elif data.get('content').lower() == 'linux':
            content = 'Hello Linux'
        else:
            content = 'awesome boer'
    msgtype = 'text'
    reply_xml = '''
        <xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[%s]]></MsgType>
        <Content><![CDATA[%s]]></Content>
        </xml>
    '''
    reply = reply_xml % (tousername, fromusername, createtime, msgtype, content)
    return reply