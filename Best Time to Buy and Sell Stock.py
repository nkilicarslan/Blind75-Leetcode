class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # decleare two pointer in order to iterate over the array
        left_ptr = 0
        right_ptr = 1
        # decleare a var to keep max value and firstly assign it to 0
        max_value = 0
        # check the right pointer if right pointer is out of the border break it
        while right_ptr < len(prices):
            # check whether right ptr value is greater than left ptr value
            if prices[right_ptr] - prices[left_ptr] > 0:
                # check the difference of the pointers
                if prices[right_ptr] - prices[left_ptr] > max_value:
                    # if the value is greater than max value, update it
                    max_value = prices[right_ptr] - prices[left_ptr]
                # move the pointer to the right
                right_ptr+= 1
            else:
                # update the pointers
                left_ptr = right_ptr
                right_ptr += 1
        # return the maximum value
        return max_value