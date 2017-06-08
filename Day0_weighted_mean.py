# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:19:45 2017

@author: George
"""

#size = int(input())
#num = list(map(int,input().split()))
#weights = list(map(int,input().split()))

size = 5
nums = [10, 40, 30, 50, 20]
weights = [1, 2, 3, 4, 5]
print (round((sum([weights[i] * nums[i] for i in range(size)]) / sum(weights)), 1))
