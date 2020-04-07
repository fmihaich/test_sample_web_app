import json
import requests
import os

SERVER_URL = 'http://' + os.environ['SERVER_HOST'] + ':' + os.environ['SERVER_PORT']

# API ENDPOINTS
SERVER_ADD_USER_URL = SERVER_URL + '/user/add'
SERVER_GET_USERS_URL = SERVER_URL + '/users'


def add_user(user_info):
    try:
        return requests.post(
            url=SERVER_ADD_USER_URL, data=json.dumps(user_info),
            headers={"Content-Type" : "application/json"})
    except:
        return None


def get_users():
    try:
        return requests.get(url=SERVER_GET_USERS_URL)
    except:
        return None
