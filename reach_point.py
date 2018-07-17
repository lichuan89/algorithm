#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note
"""


def reach_point(sx, sy, tx, ty):
    """
    规则: (sx, sy) -> (sx + sy, sy) or (sz, sx + sy)
    目标: sx, sy 通过转换是否能达到tx, ty?
    解法: tx, ty(tx > ty)一定是tx%ty, ty转换的
    """ 
    while tx >= sx and ty >= sy:
        if tx > ty:
            tx %= ty;
        else:
            ty %= tx;
    if tx == sx:
        return (ty - sy) % sx == 0;
    if ty == sy:
        return (tx - sx) % sy == 0;
    return False;


def reach_point_v2(sx, sy, tx, ty):
    """
    规则: (sx, sy) -> (sx + sy, sy) or (sz, sx + sy)
    目标: sx, sy 通过转换是否能达到tx, ty?
    解法: tx, ty(tx > ty)一定是tx%ty, ty转换的
    """ 
    while sx <= tx and sy <= ty:
        if tx > ty:
            if ty == sy:
                return (tx - sx) % ty == 0 
            else:
                tx %= ty
        else:
            if tx == sx:
                return (ty - sy) % tx == 0
            else:
                ty %= tx
    return sx == tx and sy == ty 
    
    

if __name__ == "__main__":
    print reach_point(1, 1, 2, 2) 
    print reach_point(1, 1, 1, 1) 
