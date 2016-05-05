# -*- coding: utf-8 -*-

import re

import config
import discuz
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class Post(discuz.Discuz):

    def __init__(self):
        super(Post, self).__init__()
        print 'Post'
        self.post_success_pattern = re.compile(
            r'<meta name="keywords" content="(?u)(.+)" />')  # 发帖成功时匹配
        self.post_fail_pattern = re.compile(
            r'<div id="messagetext" class="alert_error">')  # 发贴失败时匹配
        self.post_error_pattern = re.compile(r'<p>(?u)(.+)</p>')  # 发贴失败的错误信息

    def newthread(self, fid, subject, message):
        postdata = {
            'subject': self._interception(subject, 80),
            'message': message,
            'formhash': self.formhash,
        }

        base_url = config.POSTURL
        url = base_url.replace('FID', fid)
        self.operate = self._get_response(url, postdata)

        prefix = '主题 "%s" ' % postdata['subject']
        self.__verify_post_status(prefix)

    def reply(self, tid, message):
        postdata = {
            'message': message,
            'formhash': self.formhash,
        }

        base_url = config.REPLYURL
        url = base_url.replace('TID', tid)
        self.operate = self._get_response(url, postdata)

        prefix = '回复 "%s" ' % self._interception(message, 80)
        self.__verify_post_status(prefix)

    def __verify_post_status(self, prefix):
        page_content = self.operate.read()

        if self.post_success_pattern.search(page_content):
            print "%s发布成功！" % prefix
        elif self.post_fail_pattern.search(page_content):
            post_error_message = self.post_error_pattern.search(page_content)
            try:
                print "%s发布失败！原因是：%s。" % (prefix, post_error_message.group(1))
            except:
                print "%s发布失败！原因是：未知原因。" % prefix
        else:
            print "无法确定%s发布状态" % prefix
