class Solution:
    # The function takes a 2D matrix and a target value, and returns True if the target is found in the matrix, otherwise returns False.
    def searchMatrix(self, matrix, target):
        # Check for empty matrix
        if not matrix or not matrix[0]:
            # If the matrix is empty or the first row is empty, return False
            return False

            # Get the number of rows (m) and columns (n) in the matrix
        m, n = len(matrix), len(matrix[0])
        # Initialize pointers for the current position
        row, col = 0, n - 1

        # Loop until we are within the bounds of the matrix
        while row < m and col >= 0:
            # Compare the current element with the target
            if matrix[row][col] == target:
                # If the current element is equal to the target, return True
                return True
            # If the current element is greater than the target, move left to find smaller values
            elif matrix[row][col] > target:
                # If the current element is greater than the target, move left to find smaller values 
                col -= 1
            # If the current element is less than the target, move down to find larger values    
            else:
                # If the current element is less than the target, move down to find larger values
                row += 1

        # If we exit the loop without finding the target, return False
        return False
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(sol.searchMatrix(matrix, target))  # Output: True

    target2 = 20
    print(sol.searchMatrix(matrix, target2))  # Output: False