#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def maximum_array(arr):
    """ 
    数组先生序后将序, 求最大元素
    """
    if arr == []: 
        return None
    begin, end = 0, len(arr) - 1 
    while begin <= end:
        mid = (begin + end) / 2 
        # 只有1个或2个元素
        if begin == end or begin == end - 1:
            return max(arr[begin], arr[end])
        # mid左边是生序
        elif mid == 0 or arr[mid - 1] < arr[mid]:
            begin = mid 
        # mid右边是降序
        elif mid == len(arr) - 1 or arr[mid] > arr[mid + 1]: 
            end = mid 

 
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 4, 3, 1]
    print maximum_array(arr)
