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


size = int(input())
nums = list(map(int,input().split()))
mult = list(map(int,input().split()))

#size = list(map(int,"6 12 8 10 20 16".split()))
#mult = list(map(int,"5 4 3 2 1 5".split()))
#n = len(nums)

interquartile = []

for x in range(0, size):
    interquartile += [nums[x]] * mult[x]

quart = quartile(interquartile)

print (float(round((quart[2] - quart[0]),1)))

    