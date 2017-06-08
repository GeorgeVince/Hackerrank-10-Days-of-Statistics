# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:15:56 2017

@author: George
"""

import collections

#size = int(input())
#nums = sorted(list(map(int,input().split())))

size = 10
nums =  sorted([64630,11735,14216,99233,14470,4978,73429,38120,51135,67060])

#Mean
counts = collections.Counter(nums)
total = [val * count for val, count in counts.items()]
mean = sum(total) / len(total)



#Median
middle, is_odd_length = divmod(size, 2)

if is_odd_length:
    median = nums[middle]
    
else:
    median = (nums[middle - 1] + nums[middle]) / 2


    
#Mode
freq = 0
mode = 0

for key, val in counts.items():
    if val > freq:
        mode = key
        freq = val
        
    elif val == freq and key < mode:
        mode = key


print (mean)
print (median)
print (mode)  