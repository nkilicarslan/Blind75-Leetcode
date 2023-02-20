def helper(n, total_step_numbers):
    # if the value is calculated or known directly return that value
    if n in total_step_numbers:
        return total_step_numbers[n]
    else:
        # save that value in the dict
        total_step_numbers[n] = helper(n-1,total_step_numbers) + helper(n-2,total_step_numbers)
        # return that value
        return total_step_numbers[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        #    define a dict to keep the results
        total_step_numbers = {}
        # define the base case results
        total_step_numbers[1] = 1
        total_step_numbers[2] = 2
        # if n value is known directly return that value
        if n in total_step_numbers:
            return total_step_numbers[n]
        # else find the value with helper function
        return helper(n-1,total_step_numbers) + helper(n-2,total_step_numbers)