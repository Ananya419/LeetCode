from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        if n == 0:
            return 0
            
        robots_data = sorted(zip(robots, distance))
        R = [r for r, d in robots_data]
        D = [d for r, d in robots_data]
        
        walls_set = set(walls)
        robots_set = set(R)
        
        base_ans = 0
        W_clean = []
        for w in walls_set:
            if w in robots_set:
                base_ans += 1
            else:
                W_clean.append(w)
                
        W = sorted(W_clean)
        
        def get_count(left: int, right: int) -> int:
            if left > right:
                return 0
            return bisect_right(W, right) - bisect_left(W, left)
            
        dp = [[0, 0] for _ in range(n)]
        
        dp[0][0] = get_count(R[0] - D[0], R[0] - 1)
        dp[0][1] = 0
        
        for i in range(1, n):
            I1_L = R[i-1] + 1
            I1_R = min(R[i] - 1, R[i-1] + D[i-1])
            val_prev_R = get_count(I1_L, I1_R)
            
            I2_L = max(R[i-1] + 1, R[i] - D[i])
            I2_R = R[i] - 1
            val_curr_L = get_count(I2_L, I2_R)
            
            if I1_L <= I1_R and I2_L <= I2_R:
                ov_L = max(I1_L, I2_L)
                ov_R = min(I1_R, I2_R)
                overlap = get_count(ov_L, ov_R)
            else:
                overlap = 0
                
            opt1 = dp[i-1][0] + val_curr_L
            opt2 = dp[i-1][1] + val_prev_R + val_curr_L - overlap
            dp[i][0] = max(opt1, opt2)
            
            opt3 = dp[i-1][0]
            opt4 = dp[i-1][1] + val_prev_R
            dp[i][1] = max(opt3, opt4)
            
        ans = max(
            dp[n-1][0], 
            dp[n-1][1] + get_count(R[n-1] + 1, R[n-1] + D[n-1])
        )
        
        return ans + base_ans



# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    robots = [1, 5, 10]
    distance = [2, 3, 1]
    walls = [2, 4, 6, 9]
    print(sol.maxWalls(robots, distance, walls))  # Output: 3
    