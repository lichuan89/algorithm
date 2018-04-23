#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def search_rotate_array(arr, x):
    """
    排序数组arr[0: n]旋转为arr[m: n] + arr[0: m]
    查找数字是否在数组中
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == x:
            return mid
        elif arr[low] <= x < arr[mid]:
            high = mid - 1
        elif arr[mid] < x <= arr[high]:
            low = mid + 1
        elif arr[low] <= arr[mid]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [3, 4, 5, 7, 0, 1, 2]
    print search_rotate_array(arr, 1)
    print search_rotate_array(arr, 5)
    print search_rotate_array(arr, 6)
