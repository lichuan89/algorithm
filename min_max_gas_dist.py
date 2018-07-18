#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note
"""

def min_max_gas_dist(stations, k):
    """
    min_max_gas_dist
    """
    dists = [[i, stations[i] - stations[i -1]] for i in range(1, len(stations))]
    for _ in range(k):
        # 最大距离
        max_i = 1
        for t in range(len(dists)):
            if dists[t][1] > dists[max_i][1]:
                max_i = t 
        # 该距离曾经是某个距离分成j份，则现在重新分成j+1份
        d = sum([v[1] for v in dists if v[0] == dists[max_i][0]])
        j = len([v[1] for v in dists if v[0] == dists[max_i][0]])
        dists.append([dists[max_i][0], 0])
        for t in range(len(dists)):
            if dists[t][0] == dists[max_i][0]:
                dists[t][1] = float(d) / (j + 1)
    return max([v[1] for v in dists])


def min_max_gas_dist_v2(stations, k):
    """
    min_max_gas_dist
    """
    dists = [stations[i] - stations[i -1] for i in range(1, len(stations))]
    left = 0
    right = max(dists)
    while left < right - 0.00001:
        mid = (left + right) / 2.0
        n = 0
        for d in dists:
            n += int(d / mid) - 1 +  (1 if (d % mid) != 0 else 0)
        if n <= k:
            right = mid
        else:
            left = mid
    return left

if __name__ == "__main__":
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 9
    print min_max_gas_dist(stations, k)
    print min_max_gas_dist_v2(stations, k)
    stations = [10, 19, 25, 27, 56, 63, 70, 87, 96, 97]
    k = 3 
    print min_max_gas_dist(stations, k) 
    print min_max_gas_dist_v2(stations, k)
