import pdb
import sys

class Result:
    left = 0
    right = 0
    sumValue = 0

def find_maximum_subarray(A):

    result = Result()
    result.left = 0
    result.right = 0
    result.sumValue = -sys.maxsize

    for index in range(len(A)):
        sumValue = A[index]

        for item in range(index+1, len(A)):
            sumValue += A[item]

            if sumValue > result.sumValue:
                result.left = index
                result.right = item
                result.sumValue = sumValue
    return result

a = [-1,2,3,4,-5]
pdb.set_trace()
result = find_maximum_subarray(a)
print('a = ', a)
print('left = ', result.left)
print('right = ', result.right)
print('sum = ', result.sumValue)
