# -*- coding: utf-8 -*-
__author__ = "shizhiwei"
# @Time    : 2020/10/26 10:37
# Email    : shizhiwei@canway.net
# instruction : 用来测试一些方法
import base64

if __name__ == '__main__':
    str_one = "1 2020"
    encode_str = base64.b64encode(str_one.encode('utf-8')).decode('utf-8')
    decode_str = base64.b64decode(encode_str.encode('utf-8')).decode('utf-8')
    print(encode_str)
    print(decode_str)
