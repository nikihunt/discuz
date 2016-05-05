#-*- coding: utf-8 -*-

import os
import sys
import logging
import time


class MyLogger(object):

    def __init__(self):
        self.slogger = ''
        self.flogger = ''

    # 获取当前时间
    def getCurrentTime(self, TimeFormat="%Y-%m-%d-%X"):
        return time.strftime(TimeFormat, time.localtime())

    # 设置log,sys.path[0]为当前脚本所在目录
    def setFLogger(self, LogDestination=sys.path[0], LogLevel=logging.NOTSET):
        self.flogger = logging.getLogger()
        dirpath = LogDestination + os.sep + getCurrentTime("%Y-%m-%d")
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        # 不能用getCurrentTime("%X")，因为%X格式（h:m:s）中带有":"符号，而文件名中不能出现该符号
        LogDestination = dirpath + os.sep + getCurrentTime("%H") + ".log"
        logHandler = logging.FileHandler()(LogDestination)

        self.flogger.addHandler(logHandler)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        logHandler.setFormatter(formatter)
        self.flogger.setLevel(LogLevel)

    def setSLogger(self, LogLevel=logging.NOTSET):
        self.slogger = logging.getLogger()
        logHandler = logging.StreamHandler()
        self.slogger.addHandler(logHandler)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        logHandler.setFormatter(formatter)
        self.slogger.setLevel(LogLevel)
        self.slogger

    def test(self):
        self.setSLogger()
        self.slogger.debug("logger is ready")

if __name__ == '__main__':
    MyLogger().test()
