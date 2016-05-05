# -*- coding: utf-8 -*-

import config
import myLogger
import post
import re
import time


class Info(post.Post, myLogger.MyLogger):

    def __init__(self):
        super(Info, self).__init__()
        self.typeid_pattern = re.compile(
            '<a href=\"http://www.chdchd.com/forum.php\?mod=forumdisplay&amp;fid=([0-9]+)&amp;filter=typeid&amp;typeid=([0-9]+)\">(.*)<span class=\"xg1 num\">([0-9]+)</span></a></li>')
        self.pagenum_pattern = re.compile(
            '<span title=\".{2} ([0-9]+) .{2}\">')
        # self.tid_pattern = re.compile(
        #    'http://www.chdchd.com/forum.php\?mod=viewthread&tid=([0-9]+)')
        self.tid_filename_pattern = re.compile(
            ' <a href=\"http://www.chdchd.com/forum.php\?mod=viewthread&amp;tid=([0-9]+)(.*)>(.*)</a>')
        self.typeid = {}
        self.page = {}
        self.info = {}
        self.setSLogger()

    def getTypeId(self):
        for fid in config.FIDList:
            self.slogger.debug(fid)
            if fid not in self.typeid:
                self.typeid[fid] = []
            url = config.INITURL.replace('FID', fid)
            self.operate = self._get_response(url)
            type_page = self.operate.read()
            type_info = self.typeid_pattern.findall(type_page)
            for typeinfo in type_info:
                id = typeinfo[1]
                typename = typeinfo[2]
                self.typeid[fid].append(id)
                self.slogger.debug(id)

    def getPageNum(self):
        base_url = config.PAGEURL
        if len(self.typeid) > 0:
            for fid, typeidList in self.typeid.items():
                if len(typeidList) > 0:
                    if fid not in self.page:
                        self.page[fid] = {}
                    for typeid in typeidList:
                        time.sleep(config.GETINFOSLEEPT)
                        url = base_url
                        url = url.replace('FID', fid).replace('TYPEID', typeid)
                        self.slogger.debug(url)
                        try:
                            self.operate = self._get_response(url)
                            page = self.operate.read()
                            info = self.pagenum_pattern.findall(page)
                            pagenum = 1
                            if info:
                                pagenum = info[0]
                            self.page[fid][typeid] = pagenum
                            self.slogger.debug(fid)
                            self.slogger.debug(typeid)
                            self.slogger.debug(pagenum)
                            self.slogger.debug("--------------------")
                        except Exception, e:
                            self.slogger.debug("error----------" + url)

    def getTID(self):
        base_url = config.TIDURL
        if len(self.page) > 0:
            for fid, TypeidAndPageDict in self.page.items():
                if len(TypeidAndPageDict) > 0:
                    for typeid, pagesum in TypeidAndPageDict.items():
                        num_list = []
                        pagesum = int(pagesum)
                        if pagesum > 5:
                            num_list = range(5, pagesum + 1)[::2]

                        for pagenum in num_list:
                            # 获取每个网页后程序睡眠一定时间，防止被server误认为DDOS攻击
                            time.sleep(config.GETINFOSLEEPT)
                            url = base_url.replace('FID', fid).replace(
                                'TYPEID', typeid).replace('PAGENUM', str(pagenum))
                            self.slogger.debug(url)
                            try:
                                self.operate = self._get_response(url)
                                page = self.operate.read()
                                info = self.tid_filename_pattern.findall(page)
                                key = config.SEP.join(
                                    [fid, typeid, str(pagesum), str(pagenum)])
                                if key not in self.info:
                                    self.info[key] = {}
                                if info:
                                    with open(key + '.data', 'w') as f:
                                        for value in info:
                                            if len(value) == 3:
                                                self.info[key][
                                                    value[0]] = value[2]
                                                f.write(
                                                    value[0] + config.SEP + value[2] + '\n')
                                self.slogger.debug(
                                    key + " : " + str(len(info)))
                            except Exception, e:
                                self.slogger.debug("error----------" + url)
                                config.GETINFOSLEEPT = config.GETINFOSLEEPT + config.GAP
