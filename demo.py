# -*- coding: utf-8 -*-
# @ create time: 2018/9/16 15:47
# @ file name: demo.py
# @ IDE: PyCharm
# @ author: hou


import json
import requests

from log_pack import Logging
from main import Get_server_res

logger = Logging.logger()


url_step1 = "https://e.sm.cn/api/report/getReport"
url_step2 = "https://e.sm.cn/api/task/getTaskState"
url_step3 = "https://e.sm.cn/api/file/downloade"

step1_body = {
        "startDate": "2018-08-19",
        "endDate": "2018-09-10",
        "reportType":2
    }

res_step1 = Get_server_res().request_initiation(url_step1, step1_body)
logger.info("step1 response --> res_step1: {}".format(res_step1))

taskId = {"taskId": json.loads(res_step1)[u'body'][u'taskId']}

res_step2 = Get_server_res().request_initiation(url_step2, taskId)

logger.info("step2 response --> taskId: %s, res_step2: %s" % (taskId, res_step2))
fileId = {"fileId": json.loads(res_step2)[u'body'][u'fileId']}

res_step3 = Get_server_res().request_initiation(url_step3, fileId)
logger.info("step3 response --> fileId: %s, res_step3: %s" % (fileId, res_step3))