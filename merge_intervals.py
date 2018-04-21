#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def merge_intervals(arr):
    """ 
    合并区间 
    """
    if len(arr) == 1:
        return arr 
    # 对所有区间按开始位置排序
    regions = {}
    for (a, b) in arr:
        if a not in regions or b > regions[a]:
            regions[a] = b 
    begins = regions.keys()
    begins.sort()
    regions = [[begin, regions[begin]] for begin in begins]
    
    # 从小到大合并区间 
    merge_regions = []
    region = regions[0]
    for i in range(1, len(regions)):
        a, b = regions[i]
        if region[1] >= a:
            region[1] = max(region[1], b)
        else:
            merge_regions.append(region)
            region = [a, b]
    merge_regions.append(region)
    return merge_regions

if __name__ == "__main__":
    arr = [[1,3],[2,6],[8,10],[15,18]]
    print merge_intervals(arr)
