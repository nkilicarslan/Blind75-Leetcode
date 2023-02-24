from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # create a variable to keep row count
        row_count = len(matrix)
        # create a variable to keep column count
        column_count = len(matrix[0])
        # create a dict to keep indexes will be updated to 0
        keep_the_0_row_and_column = {}
        # iterate over the matrix array
        for i in range(row_count):
            for j in range(column_count):
                # if the instant value is 0
                if matrix[i][j] == 0:
                    # store the 0 values for that row
                    for k in range(column_count):
                        keep_the_0_row_and_column[(i, k)] = 1
                    # store the 0 values for that column
                    for k in range(row_count):
                        keep_the_0_row_and_column[(k, j)] = 1
        # iterate over the matrix and update the necassary indexes to 0
        for i in range(row_count):
            for j in range(column_count):
                # if the instant value in the hash, update it to 0
                if (i,j) in keep_the_0_row_and_column:
                    matrix[i][j] = 0
