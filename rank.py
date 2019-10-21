# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         rank.py
# Description:  排序算法：
#                       1.1 冒泡<bubbling>
# Author:       xuanguoke
# Date:         2019/10/17
#-------------------------------------------------------------------------------
import random
# 生成无序列表

disorder_list = []
for i in range(0,1000):
    disorder_list.append(random.randint(1, 1000000))

print(disorder_list)


# 1.1 冒泡排序
# 思路：
#       1. 每次从<无序区>找到最小值，放到<有序区>的末尾；
#       2. 重复<n-1> 次，即可获得有序列表