# -*- coding: utf-8 -*-

#------------------------------------全局设置-----------------------------------
DOMAIN = r'http://www.chdchd.com/'
COOKIETIME = 2592000
CODE = r'gbk'
SEP = '-'
SLEEPT = 2
GETINFOSLEEPT = 5
REPLYTIME = 15
GAP = 5
DEFAULT_COMMENT = "，很不错的电影，重温一下！"
LOOPTIME = 60*60
#------------------------------------登录模块--------------------------------------
USERNAME = ''
PASSWORD = ''

LOGINFIELD = r'username'


HOMEURL = DOMAIN + r'forum.php'
LOGINURL = DOMAIN + \
    r'member.php?mod=logging&action=login&loginsubmit=yes&frommessage&inajax=1'


#-----------------------------------发帖和回复模块-----------------------------------
POSTURL = DOMAIN + r'forum.php?mod=post&action=newthread&fid=FID&extra=&topicsubmit=yes'
REPLYURL = DOMAIN + r'forum.php?mod=post&action=reply&tid=TID&extra=&replysubmit=yes'


#-----------------------------------获取信息(typeid,tid,pagenum)--------------
FIDList = ['39', '40']
INITURL = DOMAIN + r'forum.php?mod=forumdisplay&fid=FID'  # 获取typeid
PAGEURL = DOMAIN + \
    r'forum.php?mod=forumdisplay&fid=FID&filter=typeid&typeid=TYPEID'  # 获取pagenum
TIDURL = DOMAIN + r'forum.php?mod=forumdisplay&fid=FID&filter=typeid&typeid=TYPEID&page=PAGENUM'  # 获取tid
