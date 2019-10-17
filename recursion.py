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

# 方案二：

