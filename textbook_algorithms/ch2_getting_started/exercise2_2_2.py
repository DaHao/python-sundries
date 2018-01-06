# coding=utf-8
"""
Date: 2018-01-06
Author: Sheng Hao
Description:
    Selection Sort選擇排序法實作，並說明best case，worse case時間複雜度
"""

def selectionSort(arr):
    for index in range(len(arr) - 1):
        minIndex = findMinIndex(arr[index:], index)
        if index != minIndex:
            exchange(arr, index, minIndex)
    return arr

def exchange(arr, i, j):
    """ 交換陣列值 """
    arr[i], arr[j] = arr[j], arr[i]

def findMinIndex(arr, shift):
    """ 找出最小值的索引值，因為不是原陣列，所以要加上偏移量 """
    minIndex, minValue  = 0, arr[0]
    for index, value in enumerate(arr):
        if value < minValue:
            minIndex, minValue = index, value

    return minIndex + shift


if __name__ == "__main__":
    arr = [7,3,5,9,2,8,4]
    print(selectionSort(arr))
