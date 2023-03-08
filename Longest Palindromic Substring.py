class Solution:
    def longestPalindrome(self, s: str) -> str:
        # create a variable to keep the maximum value
        max_value = 0
        # create a variable to keep the longest palindrome
        longest_palind = ''
        # iterate over the string
        for i in range(len(s)):
            # create two pointers to keep track of the left and right
            left_ptr, right_ptr = i, i
            # while the pointers are in the range of the string
            # this is for even length palindromes
            while left_ptr>=0 and right_ptr < len(s):
                # if the chars are equal
                if s[left_ptr] == s[right_ptr]:
                    # if the new value is bigger than the old value
                    if max_value < right_ptr - left_ptr +1:
                        # update the max value
                        max_value = right_ptr - left_ptr + 1
                        # update the longest palindrome
                        longest_palind = s[left_ptr:right_ptr + 1]
                    # update the pointers
                    left_ptr -= 1
                    right_ptr += 1
                # if the chars are not equal break the loop
                else:
                    break
            # create two pointers to keep track of the left and right
            # this is for odd length palindromes
            left_ptr, right_ptr = i, i+1
            # while the pointers are in the range of the string
            while left_ptr >= 0 and right_ptr < len(s):
                # if the chars are equal
                if s[left_ptr] == s[right_ptr]:
                    # if the new value is bigger than the old value
                    if max_value < right_ptr - left_ptr + 1:
                        # update the max value
                        max_value = right_ptr - left_ptr + 1
                        # update the longest palindrome
                        longest_palind = s[left_ptr:right_ptr + 1]
                    # update the pointers
                    left_ptr -= 1
                    right_ptr += 1
                # if the chars are not equal break the loop
                else:
                    break
        # return the longest palindrome
        return longest_palind
