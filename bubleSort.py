def bubleSort(arr):
    idx = 0
    while(idx < len(arr)):
        keyVal = arr[idx]
        MoveVal(arr, keyVal)
        idx += 1
            
def switchVal(arr, valA, valB):
    i, j = arr[valA], arr[valB]
    arr[i], arr[j] = arr[j], arr[i]
    
def MoveVal(arr, Val):
    idx = arr.index(Val)
    while(idx + 1 < len(arr)):
        if(arr[idx] > arr[idx+1]):
            switchVal(arr, idx, idx+1)
            idx += 1
        else:
            break

arr = [3, 2, 1]
bubleSort(arr)
print(arr)
