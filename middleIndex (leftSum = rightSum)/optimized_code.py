from ast import List


def findMiddleIndex(self, nums: List[int]) -> int:
    Prefix_Sum = [0] * len(nums)        #Intialize with 0 and length will be same sa nums
    
    Prefix_Sum[0] = nums[0]             #Assign first value of nums to prefix sum
    
    for i in range(1,len(nums)):                    # Loop from 1 to length of nums
        Prefix_Sum[i] = Prefix_Sum[i-1] + nums[i]  # Keep adding previous value to current value
        
    for i in range(len(nums)):
        
        if i==0:
            left = 0
        else:
            left =  Prefix_Sum[i-1]
            
        
        if i==len(nums)-1:
            right=0
        else:
            right = Prefix_Sum[len(nums)-1] - Prefix_Sum[i] 
            
            
        if left == right:
            return i
    
    return -1
        