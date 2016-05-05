# -*- coding: utf-8 -*-

import config
import post
import os
import sys
import re
import time


FilenameList = []
TidAndFileNameDict = {}
file_pattern = re.compile(".+.data")


def getGB2312(message=None):
    if message == None:
        return config.DEFAULT_COMMENT
    else:
        return message.encode(config.CODE)


def getFileName(dirname):
    global FilenameList, file_pattern
    current_path = sys.path[0]
    target_path = current_path + os.sep + dirname
    if target_path and os.path.exists(target_path):
        if os.path.isdir(target_path):
            for filename in os.listdir(target_path):
                if filename == '.':
                    pass
                elif os.path.isdir(target_path + os.sep + filename):
                    getTidAndFileName(dirname + os.sep + filename)
                elif file_pattern.match(filename):
                    FilenameList.append(target_path + os.sep + filename)


def getTidAndFileName(dirname):
    DEFAULT_COMMENT = getGB2312(config.DEFAULT_COMMENT)
    global TidAndFileNameDict, file_pattern
    getFileName(dirname)
    if len(FilenameList) > 0:
        for filename in FilenameList:
            with open(filename, 'r') as f:
                for line in f:
                    info = line.split(config.SEP)
                    if len(info) > 1:
                        tid = info[0]
                        moviename = line[len(tid):]
                        if len(moviename) < 16:
                            moviename = info[1] + DEFAULT_COMMENT
                        TidAndFileNameDict[tid] = moviename


def showInfo():
    global TidAndFileNameDict
    getTidAndFileName('targetdata')
    if len(TidAndFileNameDict) > 0:
        print "TidAndFileNameDict : " + str(len(TidAndFileNameDict))
        # for tid, filename in TidAndFileNameDict.items():
        #     print tid + ":" + filename.decode('gbk')
    # print TidAndFileNameDict[TidAndFileNameDict.keys()[0]].decode('gbk')
    reply(TidAndFileNameDict.keys()[0], TidAndFileNameDict[
          TidAndFileNameDict.keys()[0]])


def reply(tid, message):
    if tid and message:
        my_account = post.Post()
        my_account.login(config.USERNAME, config.PASSWORD)
        my_account.reply(tid, message)


def main():
    global TidAndFileNameDict
    getTidAndFileName('targetdata')
    sleeptime = config.REPLYTIME
    if len(TidAndFileNameDict) > 0:
        for tid, message in TidAndFileNameDict.items():
            try:
                reply(tid, message)
                time.sleep(sleeptime)
            except Exception, e:
                continue
        print "Done!!!"

if __name__ == "__main__":
    # getTidAndFileName('data')
    # showInfo()
    while(True):
        try:
            main()
            time.sleep(config.LOOPTIME)
        except Exception, e:
            continue
