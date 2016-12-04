from flask import current_app, request
from .. import admin

@admin.route('/')
def index():
    return 'Hello Admin'