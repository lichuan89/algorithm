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
    """
    import heapq 
    h = []
    # 将A[0] / A[i]入堆
    for i in range(1, len(A)):
        heapq.heappush(h, (A[0] / float(A[i]), 0, i))

    while K > 0:
        v, f1, f2 = heapq.heappop(h)
        if f1 + 1 < f2: 
            heapq.heappush(h, (A[f1 + 1] / float(A[f2]), f1 + 1, f2))
        K -= 1
    return [A[f1], A[f2]]


if __name__ == "__main__":
    print kthSmallestPrimeFraction([1, 2, 3, 5, 7, 11], 3)
    print kthSmallestPrimeFraction([1, 2, 3, 5], 3)
