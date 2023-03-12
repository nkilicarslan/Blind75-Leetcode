class Solution:
    def hammingWeight(self, n: int) -> int:
        # convert int to binary
        bin_rep_of_num = bin(n)
        # create a variable to store the total count of ones
        number_of_ones  = 0
        # iterate over the binary representation of the given integer
        for char in bin_rep_of_num:
            # if the instant char is equal to '1'
            if char == '1':
                # increase the total count by 1
                number_of_ones += 1
        # return the total number of ones
        return number_of_ones
