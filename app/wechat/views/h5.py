from app.wechat import wechat
from flask import current_app

@wechat.route('/h5')
def h5():
    return current_app.config['TOKEN']