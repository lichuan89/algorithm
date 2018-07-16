#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note   二分搜索 
"""

def find(arr, target):
    """
    find
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) / 2
        if arr[mid] < target:
            left = mid + 1 # 选取右边区域
        elif arr[mid] > target:
            right = mid # 选取左边区域
        else:
            return mid
    if len(arr) == 1 and arr[0] == target:
        return 0 
    return -1


def right_closest_find(arr, target):
    """
    不小于目标值的最小元素
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) / 2 # 因为left < right, mid区间为[left, right)
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid # 如果存在多个命中值，希望往左边找到最左的命中值
    # 特殊情况
    if len(arr) > 0 and arr[-1] < target:
        return -1
    return right


def left_closest_find(arr, target):
    """
    不大于目标值的最大元素
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) / 2 # 因为left < right, mid区间为[left, right)
        if arr[mid] <= target: # 如果存在多个命中值，希望往右边找到最右边的命中值
            left = mid + 1
        else:
            right = mid
    if len(arr) > 0 and arr[0] > target:
        return -1 
    return right


if __name__ == "__main__":
    print find([2, 4, 5, 6, 9], 6)
    print right_closest_find([2, 4, 5, 6, 9], 3)
    print right_closest_find([2, 4, 6, 9], 7)
    print right_closest_find([2, 3, 3, 4, 6, 9], 3)
    print right_closest_find([2, 4, 6, 9], 1)
    print right_closest_find([2, 4, 6, 9], 10)
    print 'left_closest_find:'
    print left_closest_find([2, 4, 5, 6, 9], 3)
    print left_closest_find([2, 4, 6, 9], 7)
    print left_closest_find([2, 3, 3, 4, 6, 9], 3)
    print left_closest_find([2, 4, 6, 9], 1)
    print left_closest_find([2, 4, 6, 9], 10)
