from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # create a variable to store the maximum jump
        max_jump = 0
        # iterate over the list
        for i in range(len(nums)):
            # if the current value is bigger than the max jump
            if nums[i] > max_jump:
                # update the max jump
                max_jump = nums[i]
            # if the max_jump value is enough to reach the end
            if i + max_jump >= len(nums) - 1:
                # return True
                return True
            # if the max_jump is zero
            if max_jump == 0:
                # return False
                return False
            # decrement the max_jump in every iteration
            max_jump -= 1
