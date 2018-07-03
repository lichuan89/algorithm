#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note  
"""

chs = { 
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '12': 'L',
    '22': 'V',
    '26': 'Z',
}

def get_decode_num(s):
    """ 
    数字解码成字母的方法总数
    """
    # 空
    if s == '': 
        return 0
    # 1个数字
    if len(s) == 1 and s in chs:
        return 1
    n = 0 
    # 2个数字
    if len(s) == 2:
        if s in chs:
            n += 1
        if s[0] in chs and s[1] in chs:
            n += 1
        return n
    # 3个数字
    n += get_decode_num(s[: -1])
    if s[-2: ] in chs:
        n += get_decode_num(s[: -2])
    return n


if __name__ == "__main__":
    print get_decode_num('12')
    print get_decode_num('226')
