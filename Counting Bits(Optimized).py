class Solution:
    def countBits(self, n: int) -> List[int]:
        # create a list to store the result
        result_list = [0 for i in range(n+1)]
        # iterate over the range of n+1
        for i in range(1,n+1):
            # if the current number is even
            if i % 2 == 0:
                # append the number of ones to the result list
                result_list[i] = result_list[i//2]
            # if the current number is odd
            else:
                # append the number of ones to the result list
                result_list[i] = result_list[i//2] + 1
        # return the result list
        return result_list