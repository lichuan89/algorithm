#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def maximum_array(arr):
    """ 
    求最大和子数组 
    遍历以arr[i]为右边界的最大和子数组
    """
    begin, end, s = 0, 0, 0
    max_begin, max_end, max_s = 0, 0, 0
    for end in range(len(arr)):
        s += arr[end]
        if s > max_s:
            max_begin, max_end, max_s = begin, end, s
        if s < 0:
            begin = end + 1 
            s = 0 
    return arr[max_begin: max_end + 1]

    
if __name__ == "__main__":
    arr = [-2, 2, -3, 4, 3, -1, 2]
    print maximum_array(arr)
