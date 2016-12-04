# -*- coding: utf-8 -*-

'''note wechat'''

import hashlib

token = '123456'

def check_signature(signature, timestamp, nonce):
    '''check_signature'''
    l = [signature, nonce, token]
    l.sort()
    s = ''.join(l)
    return hashlib.sha1(s).hexdigest() == signature

# test xml parser
def xml_parser():
    data = '''
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[%s]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>
    '''
    import xml.etree.ElementTree as ET
    tree = ET.fromstring(data)
    return tree.find('ToUserName').text

print(xml_parser())