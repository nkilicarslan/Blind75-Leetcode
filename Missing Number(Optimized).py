from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # take the length of the list
        size_of_list = len(nums)
        # calculate the total sum up to the size_of_list
        total_sum = (size_of_list * (size_of_list + 1)) // 2
        # create a variable to store the sum of the list
        sum_of_list = 0
        # iterate over the list
        for i in range(size_of_list):
            # add the current number to the sum_of_list
            sum_of_list += nums[i]
        # return the difference between the total_sum and the sum_of_list
        return total_sum - sum_of_list