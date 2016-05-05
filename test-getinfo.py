# -*- coding: utf-8 -*-

import getinfo
import re


def testre():
    str = '<li><a href=\"http://www.chdchd.com/forum.php?mod=forumdisplay&amp;fid=40&amp;filter=typeid&amp;typeid=1\">动作片<span class=\"xg1 num\">1017</span></a></li>'
    typeid_pattern = re.compile(
        '<a href=\"http://www.chdchd.com/forum.php\?mod=forumdisplay&amp;fid=40&amp;filter=typeid&amp;typeid=([0-9]+)\">(.*)<span class=\"xg1 num\">1017</span></a></li>')
    str1 = '<span title=\"共 90 页\"> / 90 页</span>'
    with open('page.txt') as f:
        str1 = f.read()
    pagenum_pattern = re.compile('<span title=\".{2} ([0-9]+) .{2}\">')
    # str = 'abc12ab45de'
    # typeid_pattern = re.compile('([0-9]+)')
    filename_pattern = re.compile(
        ' <a href=\"http://www.chdchd.com/forum.php\?mod=viewthread&amp;tid=([0-9]+)(.*)>(.*)</a>')
    print filename_pattern.findall(str1)[0][0]
    filename = filename_pattern.findall(str1)[0][2]
    filename = filename.decode('gbk')
    print filename
    print type(filename)
    print len(filename_pattern.findall(str1))

if __name__ == "__main__":
    mytest = getinfo.Info()
    mytest.getTypeId()
    mytest.getPageNum()
    mytest.getTID()
    print 'done'
    # testre()
