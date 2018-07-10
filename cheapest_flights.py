#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note  
"""

def cheapest_flights(edges, src, dst, k):
    """
    转机k次以内最便宜的航线价格
    """
    if k ==0:
        return edges[(src, dst)] if (src, dst) in edges else -1
    min_cost = -1
    for (a, b), cost in edges.items():
        if a != src:
            continue
        left_cost = cheapest_flights(edges, b, dst, k - 1)
        if left_cost == -1:
            continue
        cost += left_cost
        if min_cost == -1 or cost < min_cost:
            min_cost = cost
    return min_cost
    

def cheapest_flights_v2(edges, src, dst, k):
    """
    转机k次以内最便宜的航线价格
    动态规划
    """
    dp = {(0, src): 0} # dp[(i,j)]表示最多转机i次到达城市j的最便宜价格
    for (a, b), cost in edges.items():
        if a == src:
            dp[(0, b)] = cost
    for n in range(1, k + 1):
        for (a, b), cost in edges.items():
            if (n - 1, a) in dp:
                dis = dp[(n-1, a)] + cost
                if (n, b) not in dp or dp[(n, b)] > dis:
                    dp[(n, b)] = dis
    if (k, dst) in dp:
        return dp[k, dst]
    else:
        return -1


if __name__ == "__main__":
    edges = {(0, 1): 100, (1,2): 100, (0,2): 500}
    print cheapest_flights(edges, 0, 2, 1)
    print cheapest_flights(edges, 0, 2, 0)
    print cheapest_flights_v2(edges, 0, 2, 1)
    print cheapest_flights_v2(edges, 0, 2, 0)
