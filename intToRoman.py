!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note  
"""

def f(num, lowCh, highCh, nextLowCh):
    """ 
    某一位数字转换为罗马数字
    """
    if num < 4:
        return num * lowCh 
    elif num == 4:  
        return lowCh + highCh
    elif 9 > num >= 5:
        return highCh + (num - 5) * lowCh
    else:
        return lowCh + nextLowCh


def intToRoman_v2(num):
    """
    整数转换为罗马数字
    """
    s = ''

    if num / 1000 > 0:
        s += f(num / 1000, 'M', '-', '-')
        num = num % 1000
    if num / 100 > 0:
        s += f(num / 100, 'C', 'D', 'M')
        num = num % 100
    if num / 10 > 0:
        s += f(num / 10, 'X', 'L', 'C')
        num = num % 10
    if num > 0:
        s += f(num, 'I', 'V', 'X')
    return s
    
   
def intToRoman(num):
    """
    整数转换为罗马数字
    """
    s = ''
    values = [
        (1000, 'M' ),
        (900,  'CM'),
        (500,  'D' ),
        (400,  'CD'),
        (100,  'C' ),
        (90,   'XC'),
        (50,   'L' ),
        (40,   'XL'),
        (10,   'X' ),
        (9,    'IX'),
        (5,    'V' ),
        (4,    'IV'),
        (1,    'I' ),
    ]
    for (i, ch) in values:
        s += (num / i) * ch
        num = num % i
    return s

if __name__ == "__main__":
    print intToRoman(1994)
    print intToRoman_v2(1994)
