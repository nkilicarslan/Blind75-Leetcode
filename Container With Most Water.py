class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE SOLUTION
        # create a variable to keep maximum value
        max_value = 0
        # iterate over the list
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                # find the bottleneck of the container
                bottleneck = min(height[i], height[j])
                # if the new area bigger than old area
                if bottleneck * (j - i) > max_value:
                    # update it
                    max_value = bottleneck * (j - i)
        # return the maximum value
        return max_value