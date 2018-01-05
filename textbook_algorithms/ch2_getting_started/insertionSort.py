# coding=utf-8
"""
date: 2018-01-05
Author: Sheng Hao
Description:
   插入排序
   將元素依序進行比較，如果比前一個小，就跟前一個交換位置，交換完後如果又比前一個小，就繼續交換位置，重複進行。
   一直到跑完整個序列，排序完成。
   時間複雜度: n平方
"""

def InsertSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr

if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    InsertSort(arr)
    print(arr)
