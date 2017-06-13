# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 20:35:28 2017

@author: George
"""

import math

#size = int(input())
#nums = sorted(list(map(int,input().split())))


nums =  sorted(list(map(int,"10 40 30 50 20".split())))
size = len(nums)
#Mean
mean = sum(nums) / size

variance = sum(list(map(lambda x: math.pow((x - mean),2), nums))) / size
std = round(variance ** 0.5,1)

print (std)