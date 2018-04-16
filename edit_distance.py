#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note  
"""

def calc_edit_distance(s1, s2):
    """ 
    计算s1和s2的编辑距离
    """
    d = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)] 
    for i in range(len(s1) + 1): 
        for j in range(len(s2) + 1): 
            if i == 0 and j == 0:
                d[i][j] = 0 
            elif i == 0:
                d[i][j] = j 
            elif j == 0:
                d[i][j] = i 
            else:
                t = 0 if s1[i - 1] == s2[j - 1] else 1
                d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + t)
    return d[len(s1)][len(s2)]


if __name__ == "__main__":
    print calc_edit_distance('abcd', 'bcmd')
    print calc_edit_distance('abcd', 'bcfe')
