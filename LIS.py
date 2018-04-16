#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def LIS(arr):
    """
    求最长升序子序列
    """
    if arr == '':
        return ''
    table = {} # value是以arr[key]结尾的最长升序子序列
    for i in range(0, len(arr)): # 递归找到以arr[i]结尾的最长升序子序列
        longarr = [arr[i]]
        for j in range(i):
            subarr = table[j]
            if subarr[-1] < arr[i]:
                tmparr = subarr + [arr[i]]
                if len(tmparr) > len(longarr):
                    longarr = tmparr
        table[i] = longarr
    maxlength = max([len(v) for v in table.values()])
    return [v for (k, v) in table.items() if len(v) == maxlength]
    
        
if __name__ == "__main__":
    arr = [1, 7, 3, 5, 9, 4, 8]
    print LIS(arr)
