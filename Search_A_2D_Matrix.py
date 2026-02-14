class Solution:
    # The matrix is treated as a sorted array. The element at index mid can be accessed using:  
    def searchMatrix(self, matrix, target):
        # Check for empty matrix
        if not matrix or not matrix[0]:
            # If the matrix is empty or the first row is empty, return False
            return False

        # Get the number of rows (m) and columns (n) in the matrix
        m, n = len(matrix), len(matrix[0])
        # Initialize left and right pointers for binary search
        left, right = 0, m * n - 1

        # Perform binary search on the virtual sorted array
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            # Map the middle index to the 2D matrix coordinates
            row, col = divmod(mid, n)
            # Get the value at the middle index
            mid_val = matrix[row][col]

            # Compare the middle value with the target
            if mid_val == target:
                # If the middle value is equal to the target, return True
                return True
            # If the middle value is less than the target, search in the right half
            elif mid_val < target:
                # Move the left pointer to mid + 1
                left = mid + 1
            # If the middle value is greater than the target, search in the left half
            else:
                # Move the right pointer to mid - 1
                right = mid - 1

        # If the target is not found, return False
        return False
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [12, 14, 16]
    ]
    target = 9
    print(sol.searchMatrix(matrix, target))  # Output: True
    