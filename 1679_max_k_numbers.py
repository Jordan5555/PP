# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109


def maxOperations(nums, k):	
	# nums.sort()
	# head = 0
	# tail = len(nums)-1
	# count = 0

	# while head < tail:

	# 	sum = nums[head] + nums[tail]

	# 	if sum == k:
	# 		count += 1
	# 		head += 1
	# 		tail -= 1 

	# 	elif sum > k:
	# 		tail -=1

	# 	else:
	# 		head += 1
			
	# return count


	# Same from 167, but errors in the output format:
    
	index_map = {}

	for index, num in enumerate(nums):

		complement = k - num

		if complement in index_map:
			return (index_map[complement], index)
		
		index_map[num] = index

	return index_map	



print(maxOperations([3,1,3,4,3], 6))
