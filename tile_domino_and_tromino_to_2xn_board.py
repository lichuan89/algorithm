#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note  
"""


def tile_domino_and_tromino_to_2xn_board(n):
    if n == 1 or n == 0: 
        return 1
    if n == 2:
        return 2
    if n >= 3:
        #f(n)   = f(n-1) + f(n-2) + 2*(f(n-3) + ...)
        #f(n-1) = f(n-2) + f(n-3) + 2*(f(n-4) + ...)
        # -> f(n) = 2*f(n-1) + f(n-3)
        return 2 * tile_domino_and_tromino_to_2xn_board(n - 1) + tile_domino_and_tromino_to_2xn_board(n - 3)
    return num

def tile_domino_and_tromino_to_2xn_board_v2(n):
    dp = {
        0: 1,
        1: 1,
        2: 2,
    }
    for i in range(3, n + 1):
        dp[i] = 2 * dp[i - 1] + dp[i - 3]
    return dp[n]
    

if __name__ == "__main__":
    print tile_domino_and_tromino_to_2xn_board(3)
    print tile_domino_and_tromino_to_2xn_board_v2(3)
