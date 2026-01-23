class Solution:
    def totalFruit(self, fruits):
        left = 0
        max_fruits = 0
        last_seen = {}
    
        for right, fruit in enumerate(fruits):
            last_seen[fruit] = right
            
            # If more than 2 types, shrink window
            if len(last_seen) > 2:
                # Find the fruit with the smallest last index
                min_index = min(last_seen.values())
                # Remove that fruit
                del_fruit = fruits[min_index]
                del last_seen[del_fruit]
                # Move left pointer
                left = min_index + 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    fruits = [1,2,1,2,3,2,2,1]
    print(f"The maximum number of fruits that can be collected is: {sol.totalFruit(fruits)}")