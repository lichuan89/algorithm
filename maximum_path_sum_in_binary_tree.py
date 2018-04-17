#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def maximum_path_sum_in_binary_tree(tree):
    """ 
    二叉树中的最大路径和
    返回(根节点为起点的最大路径和, 最大路径和)
    """
    if tree is None:
        return (0, 0)
    v = tree['data']
    left_depth, left_score = maximum_path_sum_in_binary_tree(tree.get('left'))
    right_depth, right_score = maximum_path_sum_in_binary_tree(tree.get('right'))
    depth = max([v, left_depth + v, right_depth + v]) 
    score = max([left_score, right_score, depth, v + left_depth + right_depth])
    return (depth, score)


if __name__ == "__main__":
    tree = { 
        'data': -1, 
        'left': {
            'data': 1,
            'left': {
                'data': 1,
            },  
            'right': {
                'data': 2
            }   
        },  
        'right': {
            'data': 1 
        }   
    }   
    print maximum_path_sum_in_binary_tree(tree)
