class Solution:
    def maxArea(self, height: List[int]) -> int:
        # create a variable to keep maximum area value
        max_area = 0
        # create a left_pointer and assign it to the beginning of the list
        left_pointer = 0
        # create a right pointer and assign it to end of the list
        right_pointer = len(height) - 1
        # while left pointer is smaller than right pointer
        while left_pointer < right_pointer:
            # find the bottleneck of the container
            bottleneck = min(height[left_pointer], height[right_pointer])
            # calculate the new area
            new_area = (right_pointer - left_pointer) * bottleneck
            # if the new area is greater than maximum area:
            if new_area > max_area:
                # update it
                max_area = new_area
            # if the bottleneck is the left pointer
            if bottleneck == height[left_pointer]:
                # increment the left pointer
                left_pointer += 1
            # if the bottleneck is the right pointer
            else:
                # decrement the right pointer
                right_pointer -= 1
        # return the maximum area
        return max_area
