class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # create two dp array in order to keep maximum and minimum results
        dp_max = [0 for i in range(len(nums))]
        dp_min = [0 for i in range(len(nums))]
        # initialize two arrays first element to first element of the nums list
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        # iterate over the given list
        for i in range(1,len(nums)):
            # take the (list element, multiplication of max elem and list element, multiplication of min elem and list element)
            values = (nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])
            # take max and assign them a dp array
            dp_max[i] = max(values)
            # take min and assign them a dp array
            dp_min[i] = min(values)
        # return the maximum result
        return max(max(dp_max),max(dp_min))