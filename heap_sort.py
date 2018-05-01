#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""


def adjust_heap(arr, i, num):
    """
    已知arr数组表示堆,
    arr[i + 1: num]里的子树满足最大堆，调整arr[i: ]成为最大堆
    """
    # 将根节点的值冒泡下沉到合适的位置
    while True:
        # 取最大子节点
        left = 2 * i + 1 
        right = 2 * i + 2 
        idx = None
        if left < num:
            idx = left
        if right < num and (idx is None or arr[right] > arr[left]):
            idx = right
        # 没有子节点, 结束
        if idx is None:
            break
        # 根节点比子节点小，交换; 否则结束
        if arr[i] < arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
        i = idx  
      
    
def heap_sort(arr):
    """ 
    堆排序
    """
    # 调整数组成最大堆
    for i in range(len(arr) / 2 - 1, -1, -1): 
        adjust_heap(arr, i, len(arr))
    # 选取最大值，重新调整最大堆
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        adjust_heap(arr, 0, i)
    return arr


if __name__ == "__main__":
    arr = [2, 5, 7, 1, 0, 5]
    print heap_sort(arr)
