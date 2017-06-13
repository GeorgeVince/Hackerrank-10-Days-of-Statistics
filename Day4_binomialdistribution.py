# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:40:33 2017

@author: George
"""

#bRatio, ratio = list(map(float, input().split(" ")))
bRatio = 1.09
ratio = 1

probBoy = bRatio / (bRatio + 1)
probGirl = 1 - probBoy

def factorial(num):
    if num == 0:
        return 1
    else: 
        return num * factorial(num - 1)
    
def combination(n, x):
    return factorial(n) / (factorial(x) * (factorial(n - x)))

def binominal(x, n, p):
    return combination(n,x) * (p**x) * (1-p)**(n-x)

toReturn = 0   
for i in range(3,7):
    toReturn += binominal(i, 6, probBoy)

print (round(toReturn,3))
