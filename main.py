# -*- coding: utf-8 -*-
# @ create time: 2018/9/16 15:50
# @ file name: main.py
# @ IDE: PyCharm
# @ author: hou

import json
import requests

def get_userInfo(config_name):
    with open(config_name, 'r') as fo:
        return fo.read()


class Get_server_res():

    def request_initiation(self, url_step, req_json):
        params_step = {
            "header": {
                            "username":"聚知网106",
                            "password": "CUshenma0604",
                            "token": "edaa157a-4284-4480-84e3-e95cd747b388"
                        },
            "body": req_json
        }
        res_step = requests.post( url_step,
                                  headers={"content-type": "application/json"},
                                  data=json.dumps(params_step)
                                  ).text
        return res_step
