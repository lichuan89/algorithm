# -*- coding: utf8 -*-

"""
    @author lichuan89@126.com
    @date   2016/09/12  
    @note  
"""


def merge_sort_arr(arr, low, mid, high):
    """ 
    合并2个有序数组
    """
    left, right = arr[low: mid], arr[mid: high]
    l, r = 0, 0
    idx = low 
    # 每次取两个数组指针指向的最大的元素 
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[idx] = left[l]
            l += 1
        else:
            arr[idx] = right[r]
            r += 1
        idx += 1
    return arr
    
    
def merge_sort(arr, low, high):
    """ 
    归并排序
    """
    # arr只有一个元素，则结束
    if low < high - 1:
        mid = (low + high) / 2 
        # 分而治之
        merge_sort(arr, low, mid)
        merge_sort(arr, mid, high)
        # 归并
        merge_sort_arr(arr, low, mid, high)
    return arr


if __name__ == "__main__":
    arr = [2, 5, 7, 1, 0, 5]
    print merge_sort(arr, 0, len(arr))
