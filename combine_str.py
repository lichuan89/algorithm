#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note  
"""

def check_combine_str(s1, s2, s3):
    """ 
    s1和s2是否交叉组成s3
    """
    # check[i][j] s1[:i]和s2[:j]是否交叉组成s3[:i+j]
    check = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)] 
    for i in range(len(s1) + 1): 
        for j in range(len(s2) + 1): 
            if i == j == 0:
                check[i][j] = True
            elif i == 0:
                check[i][j] = s2[: j] == s3[: j]
            elif j == 0:
                check[i][j] = s1[: i] == s3[: i]
            elif s1[i - 1] == s3[i + j - 1] and check[i - 1][j]:
                check[i][j] = True
            elif s2[j - 1] == s3[i + j - 1] and check[i][j - 1]: 
                check[i][j] = True
            else:
                check[i][j] = False
    return check[len(s1)][len(s2)]

if __name__ == "__main__":
    print check_combine_str('aabcc', 'dbbca', 'aadbbcbcac')
    print check_combine_str('aabcc', 'dbbca', 'aadbbbaccc')                                                 
