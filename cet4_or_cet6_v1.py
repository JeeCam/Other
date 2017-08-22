# -*- coding:utf-8 -*-

import json
import requests
import sys


def check_cet_id():
    try:
        user_dict = {
            "ks_xm": sys.argv[1],
            "ks_sfz": sys.argv[2],
            "jb": sys.argv[3]
        }
    except Exception:
        print '''
        使用方法
        python xx.py 李二 4432212232313xxx 1
        姓名：李二
        身份证号：4432212232313xxx
        四级为1，六级为2
        '''
        return

    json_dict = json.dumps(user_dict)

    data = {
        "action": "",
        "params": json_dict
    }

    url = "http://app.cet.edu.cn:7066/baas/app/setuser.do?method=UserVerify"

    try:
        url_content = requests.post(url, data=data).content
    except Exception, e:
        "链接不上，你可以选择再试试。"+ str(e)

    if "ks_bh" not in url_content:
        print url_content
        return

    url_content = json.loads(url_content)

    print "准考证号：".decode("utf-8") + url_content['ks_bh']
    print "姓名：".decode("utf-8") + url_content['ks_xm']
    print "身份证：".decode("utf-8") + url_content['ks_sfz']

if __name__ == '__main__':
    check_cet_id()
