class Solution:
    # Binary Search
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # Helper function to check if we can ship all packages within the given number of days with the specified capacity
        def canShip(capacity: int) -> bool:
            # Calculate the number of days needed to ship all packages with the given capacity
            used_days = 1
            # current_load keeps track of the total weight loaded on the current day
            current_load = 0
            # Iterate through each package weight
            for w in weights:
                # If adding the current package exceeds the capacity, we need to start a new day
                if current_load + w > capacity:
                    # Increment the number of days used and reset the current load for the new day
                    used_days += 1
                    # Reset the current load for the new day
                    current_load = 0
                # Add the current package weight to the current load
                current_load += w
                # If the number of days used exceeds the allowed days, we can return False early
            return used_days <= days
        
        # The minimum capacity must be at least the weight of the heaviest package, and the maximum capacity can be the sum of all weights (if we ship everything in one day).
        low, high = max(weights), sum(weights)
        # Use binary search to find the minimum capacity that allows us to ship all packages within the given number of days.
        while low < high:
            # Calculate the mid-point capacity to check
            mid = (low + high) // 2
           
            if canShip(mid):
                # If we can ship with the current mid capacity, we can try to find a smaller capacity by adjusting the high pointer.
                high = mid
                
            else:
                # If we cannot ship with the current mid capacity, we need to increase the capacity by adjusting the low pointer.
                low = mid + 1
        # After the binary search loop, low will be the minimum capacity needed to ship all packages within the given number of days.        
        return low
    
# Example Usage:
sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))  # Output: 15
print(sol.shipWithinDays([3,2,2,4,1,4], 3))  # Output: 6

