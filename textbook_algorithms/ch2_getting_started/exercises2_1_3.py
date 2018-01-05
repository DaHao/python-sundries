# coding=utf-8
"""
date: 2018-01-05
author: Sheng Hao
description:
    練習2.1-3
    Input: 序列A 及 值v
    Output: 索引值i >> v = A[i]，如果v不在序列中的話，回傳NIL
    
    時間複雜度為線性n
"""

def ex213(arr, v):
    for i in range(len(arr)):
        if v == arr[i]:
            return i
    return None

if __name__ == "__main__":
    arr = [6, 3, 9, 2, 7]
    v = 5
    print(ex213(arr, v))
