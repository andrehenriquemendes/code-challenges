# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/508/

class Solution(object):
	
	def two_sum(self, nums, target):
		complements_map = dict()
		for i in range(len(nums)):
			print(complements_map)
			if nums[i] in complements_map:
				return [complements_map[nums[i]], i]
			else:
				complement = target - nums[i]
				complements_map[complement] = i
	
	def brute_force_two_sum(self, nums, target):
		result = []
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					result = [i, j]
		
		return result


solution = Solution()
print(solution.two_sum([3,2,3], 6))