def PARENT(i):
    return i // 2

def LEFT(i):
    return 2 * i

def RIGHT(i):
    return 2 * i + 1

def ConvertIndex(i):
    return i - 1

def MAX_HEAPIFY(A, i):
    l = LEFT(i)
    r = RIGHT(i)
    
    largest = i
    if l <= len(A) and A[ConvertIndex(l)] > A[ConvertIndex(i)]:
        largest = l
    if r <= len(A) and A[ConvertIndex(r)] > A[ConvertIndex(largest)]:
        largest = r

    if largest != i:
        A[ConvertIndex(i)], A[ConvertIndex(largest)] = A[ConvertIndex(largest)], A[ConvertIndex(i)]
        MAX_HEAPIFY(A, largest)

def MAX_HEAPIFY_LOOP(A, i):
    largest = 0
    while largest != i:
        l = LEFT(i)
        r = RIGHT(i)

        largest = i
        if l <= len(A) and A[ConvertIndex(l)] > A[ConvertIndex(i)]:
            largest = l
        if r <= len(A) and A[ConvertIndex(r)] > A[ConvertIndex(largest)]:
            largest = r
        if largest != i:
            A[ConvertIndex(i)], A[ConvertIndex(largest)] = A[ConvertIndex(largest)], A[ConvertIndex(i)]
            i, largest = largest, 0

A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
MAX_HEAPIFY_LOOP(A, 3)
print(A)

def BUILD_MAX_HEAP(A):
    nonLeaf = len(A) // 2
    for i in range(nonLeaf, 0, -1):
        MAX_HEAPIFY(A, i)

A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
BUILD_MAX_HEAP(A)
print(A)

def HeapSort(A)
    BUILD_MAX_HEAP(A)
    for i in range(len(A), 1, -1):
        A[1], A[i] = A[i], A[1]
        

