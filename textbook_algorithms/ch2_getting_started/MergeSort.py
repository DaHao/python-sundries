import sys

def MergeSort(arr):

    if(len(arr) == 1):
        return arr
    else:
        tmp = len(arr) // 2
    
        arrayA = arr[:tmp]
        arrayB = arr[tmp:]
    
        return CombineArray( MergeSort(arrayA), MergeSort(arrayB) )

def CombineArray(arrA, arrB):
    i, j = 0, 0
    result = []
    
    while(i < len(arrA) or j < len(arrB)):
        valA = arrA[i] if(i < len(arrA)) else sys.maxsize
        valB = arrB[j] if(j < len(arrB)) else sys.maxsize
        
        if(valA <= valB):
            result.append(valA)
            i += 1
        else:
            result.append(valB)
            j += 1
    
    return result
    
input = [1, 3, 2]
MergeSort(input)