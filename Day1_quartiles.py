# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:21:29 2017

@author: George
"""

#n = int(input())
#nums = map(int,input().split())

def median(nums):
    middle, is_odd = divmod(len(nums),2)

    if is_odd:
         return nums[middle]
    else:
        return (nums[middle] + nums[middle - 1]) / 2
    
def quartile(nums):
    nums.sort()
    middle, is_odd = divmod(len(nums),2)

    Q1 = median(nums[0:middle])
    Q2 = median(nums)
    
    if is_odd:  
        Q3 = median(nums[middle + 1:])
    else:
        Q3 = median(nums[middle:])
        
    return [Q1, Q2, Q3]

nums = list(map(int,"3 7 8 5 12 14 21 13 18".split()))
n = len(nums)


quart = quartile(nums)    
    


print (quart[0])  
print (quart[1])
print (quart[2])