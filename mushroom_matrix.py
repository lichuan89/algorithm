#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def pass_mushroom_matrix(arr):
    """
        蘑菇阵arr, 1为蘑菇.
        从左上角走到右下角(只能往右和下走), 
        绕过蘑菇的走法概率是多少
    """
    p = [[0 for j in range(len(arr[0]))] for i in range(len(arr))] 
    for i in range(len(arr)): # 从上到下
        for j in range(len(arr[0])): # 从左到右
            if arr[i][j] == 1: # 遇到蘑菇点
                p[i][j] = 0
            elif i == 0 and j == 0: # 原点
                p[i][j] = 1
            elif i == 0: # 最上面一行 
                p[i][j] = p[i][j - 1] 
            elif j == 0: # 最左边一行
                p[i][j] = p[i - 1][j]
            else:
                p[i][j] = (p[i - 1][j] + p[i][j - 1]) * 0.5
    print p
    return p[-1][-1]
 
if __name__ == "__main__":
    arr = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ] 
    print pass_mushroom_matrix(arr)
