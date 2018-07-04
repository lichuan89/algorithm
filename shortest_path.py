#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note  
"""


def dijkstra(dp, i, j): 
    """ 
    求最短路径
    """
    dis = {i: (0, [i])} # dis[k] = (d, p)表示从i到k的最短距离为d,路径为p
    while True:
        dest, p, min_d = None, None, None
        for k in dis:
            for m in range(len(dp)):
                if m not in dis and dp[k][m] is not None:
                    d = dis[k][0] + dp[k][m]
                    if min_d is None or min_d > d:
                        dest, p, min_d = m, dis[k][1] + [m], d
        if dest is None: 
            break
        dis[dest] = min_d, p
    return dis[j]  
    

def floyd(dp):
    """ 
    求最短路径
    """
    path = [[[] for _ in dp] for _ in dp] 
    for k in range(len(dp)):
        for i in range(len(dp)):
            for j in range(len(dp)):
                # dp[i][j]表示i经过0, 1, .., k到达j的最小路径大小
                # path[i][j]表示i经过0, 1, .., k到达j的最小路径经过的中间节点
                if dp[i][k] is not None and dp[k][j] is not None:
                    d = dp[i][k] + dp[k][j]
                    if dp[i][j] is None or d < dp[i][j]:
                        dp[i][j] = d 
                        path[i][j] = path[i][k] + [k] + path[k][j] 
    return (dp, path)

if __name__ == "__main__":

    dp = [
        [None, 12, None, None, None, 16, 14],
        [12, None, 10, None, None, 7, None],
        [None, 10, None, 3, 5, 6, None],
        [None, None, 3, None, 4, None, None],
        [None, None, 5, 4, None, 2, 8],
        [16, 7, 6, None, 2, None, 9],
        [14, None, None, None, 8, 9, None],
    ]
    print dijkstra(dp, 3, 0)
    dp, path = floyd(dp)
    print dp[1][6], path[1][6]
    print dp[3][0], path[3][0]
    
