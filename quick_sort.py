#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def quick_sort(arr, low, high):
    """ 
    快排
    """
    # 结束条件: 无元素或者只有一个元素
    if low >= high:
        return arr 

    first, last = low, high
    val = arr[first]

    # 二分数组，小的数字在左，大的数字在右
    while first < last:
        # 找到右边第一个小数 
        while first < last and arr[last] >= val:
            last -= 1
        # 填坑arr[first]
        if first < last:
            arr[first] = arr[last]
            first += 1
        # 找到左边第一个大数 
        while first < last and arr[first] <= val:
            first += 1
        # 填坑arr[last]
        if first < last:
            arr[last] = arr[first]
            last -= 1
    arr[first] = val 
    quick_sort(arr, low, last - 1)
    quick_sort(arr, last + 1, high)
    return arr


if __name__ == "__main__":
    arr = [7, 5, 6, 4]
    print quick_sort(arr, 0, len(arr) - 1)
