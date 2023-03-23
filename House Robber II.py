from typing import List
class Solution:
    # this function is to find the maximum amount of money that can be robbed
    def rob(self, nums: List[int]) -> int:
        # check the length of the list is less than or equal to 3
        if len(nums) <= 3:
            # return the maximum of the list
            return max(nums)
        # create an dp array for last element
        dp_for_last = [0 for i in range(len(nums))]
        # create an dp array for first element
        dp_for_first = dp_for_last.copy()
        # create an dp array for without first and last element
        dp_for_without_first_last = dp_for_first.copy()
        # create a variable to store the first value of the nums list
        nums_first_val = nums[0]
        # create a variable to store the last value of the nums list
        nums_last_val = nums[-1]
        # create a variable to store the second value of the nums list
        nums_for_last = nums.copy()
        # create a variable to store the without first and last value of the nums list
        nums_for_without_last_first = nums.copy()
        # delete the first and last element of the nums list
        del nums[0:2]
        # delete the last element of the nums list
        del nums[-1]
        # delete the last two indexes of element of the nums_for_last list
        del nums_for_last[-2:]
        # delete the first element of nums_for_last list
        del nums_for_last[0]
        # delete the first and last element of nums_for_without_last_first list
        del nums_for_without_last_first[0]
        del nums_for_without_last_first[-1]
        # iterate over the nums list
        for i in range(len(nums_for_without_last_first)):
            # if the index 0 or 1, just assign them to the dp array
            if i < 2:
                dp_for_without_first_last[i] = nums_for_without_last_first[i]
                continue
            # if the index is 2, assign the addition of index 0 of dp array and index 2 of nums array
            if i == 2:
                dp_for_without_first_last[i] = dp_for_without_first_last[i-2] + nums_for_without_last_first[i]
                continue
            # else compare the addition of these two and take the maximum then assign it
            dp_for_without_first_last[i] = max(dp_for_without_first_last[i - 2] + nums_for_without_last_first[i], dp_for_without_first_last[i - 3] + nums_for_without_last_first[i])
        for i in range(len(nums)):
            # if the index 0 or 1, just assign them to the dp array
            if i < 2:
                dp_for_first[i] = nums[i]
                dp_for_last[i] = nums_for_last[i]
                continue
            # if the index is 2, assign the addition of index 0 of dp array and index 2 of nums array
            if i == 2:
                dp_for_first[i] = dp_for_first[i-2] + nums[i]
                dp_for_last[i] = dp_for_last[i-2] + nums_for_last[i]
                continue
            # else compare the addition of these two and take the maximum then assign it
            dp_for_first[i] = max(dp_for_first[i-2] + nums[i], dp_for_first[i-3] + nums[i])
            dp_for_last[i] = max(dp_for_last[i-2] + nums_for_last[i], dp_for_last[i-3] + nums_for_last[i])
        # return the maximum of these three
        max_with_first = max(dp_for_first) + nums_first_val
        max_with_last = max(dp_for_last) + nums_last_val
        max_without_first_last = max(dp_for_without_first_last)
        return max(max_with_last, max(max_with_first, max_without_first_last))
