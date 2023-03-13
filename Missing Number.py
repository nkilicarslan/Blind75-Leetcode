from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # create a dict to keep track of the all numbers
        nums_dict = {}
        # create a variable to store the size of the list
        size_of_list = len(nums)
        # iterate over the list
        for i in range(size_of_list):
            # assign the current number as a key and 1 as a value
            nums_dict[nums[i]] = 1
        # iterate over the range of size_of_list + 1
        for i in range(size_of_list + 1):
            # if the current number is not in the dict
            if i not in nums_dict:
                # return the current number
                return i