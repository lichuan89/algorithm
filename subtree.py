#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def isSame(tree, subtree):
    if tree is None and subtree is None:
        return True
    if tree is None or subtree is None:
        return False
    return isSame(tree.get('left'), subtree.get('left')) and isSame(tree.get('right'), subtree.get('right'))


def isSubtree(tree, subtree):
    if isSame(tree, subtree):
        return True
    if tree is not None and (isSubtree(tree.get('left'), subtree) or isSubtree(tree.get('right'), subtree)):
        return True 
    return False 


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
    subtree = { 
            'data': 1,
            'left': {
                'data': 1,
            },  
            'right': {
                'data': 2
            }
        }
    print isSubtree(tree, subtree)
