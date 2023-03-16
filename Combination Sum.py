from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # create a list to store the result
        res = []
        # create a helper function to find the combinations with backtracking
        def helper(result_list, remain_value, candidates, combinations):
            # iterate over the candidates list
            for i in candidates:
                # if the current number is equal to the remain_value
                if i == remain_value:
                    # append the combinations to the result list
                    result_list.append(combinations + [i])
                # if the current number is less than the remain_value
                elif i < remain_value:
                    # find the index of the current number
                    index_of_list = candidates.index(i)
                    # call the helper function recursively
                    helper(result_list, remain_value - i, candidates[index_of_list:], combinations + [i])
        # call the helper function
        helper(res, target, candidates, [])
        # return the result list
        return res
