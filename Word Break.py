from typing import List
class Solution:
    # this is a bottom up approach to solve the problem
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a dp array to store the values of the problem
        dp_buttom_up = [False] * (len(s) + 1)
        # set the last value to True
        dp_buttom_up[len(s)] = True
        # iterate over the dp array in the reverse order
        for i in range(len(s)-1, -1 ,-1):
            # iterate over the wordDict
            for word in wordDict:
                # if the index + length of the word is less than or equal to the length of the string and the substring is equal to the word
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    # update the dp array
                    dp_buttom_up[i] = dp_buttom_up[i+len(word)]
                # if from end to the current index is there a solution to the problem break the loop
                if dp_buttom_up[i]:
                    break
        # return the first value of the dp array
        return dp_buttom_up[0]
