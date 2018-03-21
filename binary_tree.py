#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan01@baidu.com
    @date   2016/09/12  
    @note  二叉树操作
"""


class Node(object):
    """ 
    二叉树结构体
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
  

def format_tree(tree_dict):
    """ 
    将一个表示二叉树的dict转换为树结构
    """
    if tree_dict is None: 
        return None
    data, (left, right) = tree_dict.items()[0] # {data: [left_tree, right_tree]}
    return Node(data, format_tree(left), format_tree(right))


def visit_tree(tree):
    """
    后序遍历二叉树
    """
    if tree is None:
        return []
    output = []
    if tree.right is not None:
        output += visit_tree(tree.right)
    if tree.left is not None:
        output += visit_tree(tree.left)
    output.append(tree.data)
    return output


def find_least_common_ancestor(tree, data1, data2):
    """
    寻找二叉树上两个节点的最近公共祖先
    """
    if tree is None:
        return None
    elif tree.data == data1 or tree.data == data2:
        return tree.data
    left_result = find_least_common_ancestor(tree.left, data1, data2)
    right_result = find_least_common_ancestor(tree.right, data1, data2)
    if left_result is not None and right_result is not None:
        return tree.data
    return left_result if left_result is not None else right_result


def test():
    """
    测试
    """
    tree_dict = {
        1: [
            {
                2: [
                    {
                        3: [None, None]
                    },
                    {
                        4: [None, None]
                    },
                ]
            },
            {
                5: [
                    {
                        6:[
                            None,
                            {
                                7: [None, None]
                            }
                        ]
                    },
                    None
                ]
            }
        ]
    }

    tree = format_tree(tree_dict)
    datas = visit_tree(tree)
    print datas
    ancestor = find_least_common_ancestor(tree, 3, 6)
    print ancestor


if __name__ == "__main__":
    test()
