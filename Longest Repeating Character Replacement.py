class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a dict to keep the char count
        char_count = {}
        # create a variable to keep track of the maximum value
        max_value = 0
        # create a left pointer
        left_ptr = 0
        # iterate over the whole string
        for right_ptr in range(len(s)):
            # store the new char in the dictionary
            char_count[s[right_ptr]] = 1 + char_count.get(s[right_ptr], 0)
            # move the left pointer while the condition is satisfied
            while (right_ptr-left_ptr+1) - max(char_count.values()) > k:
                # decrement the left pointer value
                char_count[s[left_ptr]] -= 1
                # increase the left pointer
                left_ptr += 1
            # update the max value
            max_value = max(max_value, right_ptr-left_ptr+1)
        # return the max value
        return max_value