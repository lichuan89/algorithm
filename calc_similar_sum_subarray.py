#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""


def calc_similar_sum_subarray(arr):
    """
    数组拆为2个子数组，2个子数组的和相差最小
    """
    num = len(arr)
    s = int(sum(arr) / 2)
    # paths[i][j]表示前i个元素中和为j的子数组
    paths = [[None for i in range(0, s + 1)] for i in range(0, num + 1)]
    # 初始化: i = 0. j = 0
    paths[0][0] = []

    # 递推
    for i in range(1, num + 1):
        for j in range(0, s + 1):
            jj = j - arr[i - 1]
            if paths[i - 1][j] is not None:
                paths[i][j] = paths[i - 1][j]
            elif jj >= 0 and paths[i - 1][jj] is not None:
                paths[i][j] = paths[i - 1][jj] + [arr[i - 1]]
    # 最接近s的子数组和
    for j in range(0, s + 1):
        diff = s - j
        if paths[num][diff] is not None:
            return paths[num][diff]


if __name__ == "__main__":
    arr = [1, 2, 4, 9, 8]
    print calc_similar_sum_subarray(arr)
