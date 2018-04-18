#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""

def serialize_binary_tree(tree):
    """ 
    序列化二叉树, 层次遍历，空叶子节点用#表示 
    """
    if tree is None:
        return []  
    arr = []
    queue = [tree]
    while queue != []: 
        node = queue[0]
        del queue[0]
        if node is not None:
            arr.append(node['data'])
            queue.append(node.get('left'))
            queue.append(node.get('right'))
        else:
            arr.append('#') 
    return arr 
    
    
def deserialize_binary_tree(arr):
    """ 
    反序列化二叉树，层次遍历，空叶子节点用#表示
    """
    if arr is []: 
        return {}
    tree = {'data': arr[0]}
    queue = [tree]
    p = 1 
    while queue != []: 
        node = queue[0]
        del queue[0]
        if arr[p] != '#':
            node['left'] = {'data': arr[p]}
            queue.append(node['left'])
        p += 1
        if arr[p] != '#':
            node['right'] = {'data': arr[p]}
            queue.append(node['right'])
        p += 1
    return tree

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
    arr = serialize_binary_tree(tree)
    t = deserialize_binary_tree(arr)
    print t
    print tree
