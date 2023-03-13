class Solution:
    def countBits(self, n: int) -> List[int]:
        # create a list to store the result
        result_list = []
        # iterate over the range of n+1
        for i in range(n+1):
            # convert the current number to binary
            binary_rep = bin(i)
            # create a variable to store the number of ones
            number_of_ones = 0
            # iterate over the binary representation of the current number
            for j in binary_rep:
                # if the instant char is equal to '1'
                if j == '1':
                    # increase the number of ones by 1
                    number_of_ones += 1
            # append the number of ones to the result list
            result_list.append(number_of_ones)
        # return the result list
        return result_list