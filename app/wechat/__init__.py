from flask import Blueprint

wechat = Blueprint('wechat', __name__, url_prefix='/wechat')

from . import views
from .views import h5