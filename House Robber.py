class Solution:
    def rob(self, nums: List[int]) -> int:
        # create an dp array
        dp = [0 for i in range(len(nums))]
        # iterate over the nums list
        for i in range(len(nums)):
            # if the index 0 or 1, just assign them to the dp array
            if i < 2:
                dp[i] = nums[i]
                continue
            # if the index is 2, assign the addition of index 0 of dp array and index 2 of nums array
            if i == 2:
                dp[i] = dp[i-2] + nums[i]
                continue
            # else compare the addition of these two and take the maximum then assign it
            dp[i] = max(dp[i-2] + nums[i], dp[i-3] + nums[i])
        # return the maximum of the dp array
        return max(dp)
