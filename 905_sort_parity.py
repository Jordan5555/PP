# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000



#On**2

def sortArrayByParity(nums): 
    
    if len(nums) == 1:

        return nums

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] %2 != 0:
                nums[i], nums[j] = nums[j], nums[i]


    return nums[::-1]

print(sortArrayByParity([0,1]))


#O(n)

def sortArrayByParity(nums): 
    
    if len(nums) == 1:
        return nums

    l1 = []
    l2 = []

    for num in nums:

        if num %2 ==0:
            l1.append(num)

        else:
            l2.append(num)
            
    return l1 + l2