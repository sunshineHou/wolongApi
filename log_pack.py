# -*- coding: utf-8 -*-
# @ create time: 2018/9/16 15:50
# @ file name: log_pack.py
# @ IDE: PyCharm
# @ author: hou


import sys
import logging


class Logging():

    @classmethod
    def logger(cls):
        logger = logging.getLogger("demo_log")
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        file_handler = logging.FileHandler("demo.log")
        file_handler.setFormatter(formatter)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.setLevel(logging.INFO)
        return logger