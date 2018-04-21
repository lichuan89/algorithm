#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def inverse_pairs(arr):
    """ 
    求数字序列的逆序对.
    """
    if len(arr) <= 1: # 递归终止条件
        return []
    n = len(arr) / 2 
    # 二分递归
    # 分组各自的结果
    pairs = inverse_pairs(arr[: n]) + inverse_pairs(arr[n: ])
    # 分组之间组合的结果
    lefts = arr[: n]
    rights = arr[n: ]
    lefts.sort()
    rights.sort()
    i = len(lefts) - 1 
    j = len(rights) - 1 
    while i>= 0 and j >= 0:
        if lefts[i] > rights[j]:
            pairs += [(lefts[i], rights[k]) for k in range(j + 1)] 
            i -= 1
        elif lefts[i] < rights[j]:
            j -= 1
        else:
            i -= 1
            j -= 1
    return pairs



if __name__ == "__main__":
    arr = [7, 5, 6, 4]
    print inverse_pairs(arr)
