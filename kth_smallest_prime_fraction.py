#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note   二分搜索 
"""


def kthSmallestPrimeFraction(A, K):
    """
    数组A存放从小到大排列的质数
    求第K小的质分数
    例如: 
    # 1/2
    # 1/3 2/3
    # 1/5 2/5 3/5
    等价于已知len(A) -1 条已排序的拉链, 求第K个数
    """
    import heapq 
    h = []
    # 将A[0] / A[i]入堆, 第i行最小值
    for i in range(1, len(A)):
        heapq.heappush(h, (A[0] / float(A[i]), 0, i))

    while K > 0:
        v, f1, f2 = heapq.heappop(h)
        if f1 + 1 < f2:
            # 更新第i行最小值
            heapq.heappush(h, (A[f1 + 1] / float(A[f2]), f1 + 1, f2))
        K -= 1
    return [A[f1], A[f2]]


def kthSmallestPrimeFraction_v2(A, K):
    """
    数组A存放从小到大排列的质数
    求第K小的质分数 
    # 1/2
    # 1/3 2/3
    # 1/5 2/5 3/5
    """
    left, right = 0, 1
    while True:
        cur_f1, cur_f2 = None, None
        num = 0
        # 二分，先看下中间值对应质分数的排名
        mid = (left + right) / 2.0 

        f2 = 1
        for f1 in range(0, len(A)): # 分子
            while f2 < len(A) and float(A[f1]) / A[f2] > mid: # 分母递增
                f2 += 1
            num += len(A) - f2 # 在A[f1]/A[i]中<=mid的值个数
            if f1 < f2 < len(A) and \
                    (cur_f1 is None or float(A[cur_f1]) / A[cur_f2] < float(A[f1]) / A[f2]):
                cur_f1, cur_f2 = f1, f2
        if num == K:
            return A[cur_f1], A[cur_f2]
        elif num < K:
            left = mid
        else:
            right = mid
            
 
if __name__ == "__main__":
    print kthSmallestPrimeFraction([1, 2, 3, 5, 7, 11], 3)
    print kthSmallestPrimeFraction([1, 2, 3, 5], 3)
    print kthSmallestPrimeFraction_v2([1, 2, 3, 5, 7, 11], 3)
    print kthSmallestPrimeFraction_v2([1, 2, 3, 5], 3)
