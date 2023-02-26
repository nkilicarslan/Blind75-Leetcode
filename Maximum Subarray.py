from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # create an dp array to apply dynamic programming
        dp = [0 for i in range(len(nums))]
        # check the length of the array
        if len(nums) > 0:
            # if length more than 0 assign first element
            dp[0] = nums[0]
        else:
            # otherwise return 0
            return 0
        # iterate over the list
        for i in range(1,len(nums)):
            # if adding new element to the previous element is more than itself, update it with sum
            if dp[i-1] + nums[i] > nums[i]:
                dp[i] = dp[i-1] + nums[i]
            else: #nums[i] > dp[i-1] + nums[i]:
                dp[i] = nums[i]
        # return the maximum of the list
        return max(dp)

