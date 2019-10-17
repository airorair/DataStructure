# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         TimeCost.py
# Description:  测试函数单元的消耗时间
# Author:       xuanguoke
# Date:         2019/10/17
#-------------------------------------------------------------------------------
import time

def timeout(func):
    def timer(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()

        print(func.__name__+"\t|--->>>>\tTotal time:{:.4}s".format(end_time-start_time))
        return result
    return timer
