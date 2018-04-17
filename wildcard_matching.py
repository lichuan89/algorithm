#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def wildcard_matching(s, p): 
    """ 
    *和?分别表示匹配0-n或0-1个字符,
    求s和p是否匹配 
    """
    # check[i][j]表示s[: i]和p[: j]是否匹配
    check = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)] 
    check[0][0] = True
    for i in range(len(s) + 1): 
        for j in range(len(p) + 1): 
            if i == j == 0:
                check[i][j] = True
            elif i == 0:
                check[i][j] = check[i][j - 1] and p[j - 1] in ['*', '?']
            elif j == 0:
                check[i][j] = False 
            else:
                c1 = check[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] in ['*', '?'])
                c2 = check[i][j - 1] and p[j - 1] in ['*', '?']
                c3 = check[i - 1][j] and p[j - 1] in ['*', '?']
                check[i][j] = c1 or c2 or c3
    return check[len(s)][len(p)]
    



if __name__ == "__main__":
    print wildcard_matching('aa', '*')
    print wildcard_matching('aa', 'a*')
    print wildcard_matching('ab', '?*')
    print wildcard_matching('aab', 'c*a*b*')
