class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert chars of string upper case to lower case
        s = s.lower()
        # remove the special character from string
        s = ''.join(char for char in s if char.isalnum())
        # create a left pointer and assign it to 0
        left_ptr = 0
        # create a right pointer and assign it to the end of the string
        rigth_ptr = len(s) - 1
        # while left pointer is smaller than right pointer
        while left_ptr < rigth_ptr:
            # if the two char is equal
            if s[rigth_ptr] == s[left_ptr]:
                # increment both left and right pointer
                left_ptr += 1
                rigth_ptr -= 1
                continue
            # if the two char is not equal
            else:
                # return False
                return False
        # if the string is palindrome return True
        return True
