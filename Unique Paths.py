class Solution:
    # return the number of unique paths
    def uniquePaths(self, m: int, n: int) -> int:
        # create a variable to store the number of unique paths
        count = 0
        # create a dp array to store the values
        dp_arr = {}
        # create a recursive function to solve the problem
        def recursive_solver(x,y):
            # if the value is already in the dp array, return it
            if (x,y) in dp_arr:
                return dp_arr[(x,y)]
            # if the solution is found, return 1
            if x == m and y == n:
                return 1
            # if out of bound, return 0
            elif x > m or y > n:
                return 0
            # else add the recursive calls and return it
            else:
                dp_arr[(x,y)] = recursive_solver(x+1,y) + recursive_solver(x, y+1)
                return dp_arr[(x,y)]
        # call the recursive function and return the value
        count = recursive_solver(1,1)
        return count
