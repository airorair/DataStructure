# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         recursion.py
# Description:  递归算法
# Author:       xuanguoke
# Date:         2019/10/17
#-------------------------------------------------------------------------------

"""
案例一：
    斐波那切数列:1,1,2,3,5,8,13
    规律：list[i] = list[i-1] + list[i-2]
"""
import TimeCost

# 方案一，递归 T() = O(n^2)。基于树模型去思考时间复杂度

def recursion_fib(n):
    if n==1 or n == 2: #递归边界
        return 1
    else:
        return recursion_fib(n-1)+recursion_fib(n-2) # 递归条件

@TimeCost.timeout
def recursion_fib_time(n):
    return recursion_fib(n)

# 方案二：使用递归速度慢的原因在于，它的重复计算。
# 所以，我们使用一个列表来存储，计算过的数据。T() = O(n) S()=O(n)。空间换时间

@TimeCost.timeout
def list_fib(n):
    fib = [1,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]

# 方案三：再次考虑到我们际计算中第n个值，不会用到n-2以前的值，
# 因此我们不需保存太多数据，节省空间。T() = O(n) S()=O(1)。
@TimeCost.timeout
def para_fib(n):
    a = 1
    b = 1
    c = 1
    for i in range(3,n+1):
        c = a + b
        a = b
        b = c
    return c

print(recursion_fib_time(30))
print(list_fib(30))
print(para_fib(30))

# 何时使用递归解决问题？
# 当一个N规模的问题，可以通过拆解一步变成，
# 一个或多个N-1规模的相同问题时，考虑使用。如汉诺塔问题......