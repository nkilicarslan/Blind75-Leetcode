class Solution:
    # this function is to rotating the matrix by 90 degrees
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # create two pointers to keep track of the left and right side of the matrix
        left_ptr = 0
        right_ptr = len(matrix) - 1
        # while the left pointer is smaller than the right pointer
        while left_ptr < right_ptr:
            # iterate over the matrix and rotate the matrix
            for i in range(right_ptr-left_ptr):
                # create a variable to keep the leftmost top value
                leftmost_top = matrix[left_ptr][left_ptr+i]
                # rotate the bottomleft to the leftmost top
                matrix[left_ptr][left_ptr+i] = matrix[right_ptr-i][left_ptr]
                # rotate the bottomright to the bottomleft
                matrix[right_ptr - i][left_ptr] = matrix[right_ptr][right_ptr-i]
                # rotate the topright to the bottomright
                matrix[right_ptr][right_ptr - i] = matrix[left_ptr + i][right_ptr]
                # rotate the leftmost top to the topright
                matrix[left_ptr + i][right_ptr] = leftmost_top
            # increase the left pointer by 1
            left_ptr += 1
            # decrease the right pointer by 1
            right_ptr -= 1
