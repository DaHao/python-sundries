# coding=utf-8
"""
Date: 2018-01-05
Author: Sheng Hao
Decription:
    輸入兩個n位的二進位數字，存在長度為n的陣列A, B。
    相加後存在長度為n+1的陣列C
    寫出程式碼
"""

def ex214(b1, b2):
    n = len(b1) if len(b1) >= len(b2) else len(b2)
    A = StringBinary2Array(b1, n)
    B = StringBinary2Array(b2, n)
    C = Adding(A, B)
    return C

def Adding(A, B):
    n = len(A)
    C = [0 for i in range(n+1)]
    carry = 0
    # zip example:
    # A = [1, 2, 3] 
    # B = [4, 5, 6] 
    # zip(A, B) = [(1,4), (2, 5), (3,6)]
    # 反轉A B陣列是為了從最低位元相加
    for index, (value1, value2) in enumerate(zip(A[::-1], B[::-1])):
        value = (value1 + value2 + carry) % 2
        carry = (value1 + value2 + carry) // 2
        C[n - index] = value
    C[0] = carry
    return C


def StringBinary2Array(b, n):
    """ 轉換二進位數字的字串為數字陣列 """
    # zfill是字串前補零的函式
    return [int(i) for i in b.zfill(n)]

if __name__ == "__main__":
    b1 = '0110'
    b2 = '1010'
    print(ex214(b1, b2))
