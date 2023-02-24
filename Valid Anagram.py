class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create to dict to keep the chars of the first string
        chars_of_the_string = {}
        # create a variable and assign the first string length to that var
        length_first_string = len(s)
        # create a variable and assign the second string length to that var
        length_second_string = len(t)
        # check the string length, if not same return false
        if length_first_string != length_second_string:
            return False
        # iterate over the first string and count each char and store
        for i in s:
            if i not in chars_of_the_string:
                chars_of_the_string[i] = 1
            else:
                chars_of_the_string[i] += 1
        # iterate over the second string and check the char count is matched or not
        for i in t:
            if i in chars_of_the_string:
                length_second_string -= 1
                chars_of_the_string[i] -= 1
                if chars_of_the_string[i] < 0:
                    return False
        if length_second_string == 0:
        # if the strings are anagram return true
            return True
        return False
