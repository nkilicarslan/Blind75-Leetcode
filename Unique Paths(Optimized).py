class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a row for bottom row
        row = [1] * n

        # iterate over the rows
        for i in range(m-1):
            # get the new row
            newrow = [1] * n
            # iterate over the columns
            for j in range(n-2,-1,-1):
                # update the value
                newrow[j] = newrow[j+1] + row[j]
            # update the row
            row = newrow
        # return the solution value
        return row[0]