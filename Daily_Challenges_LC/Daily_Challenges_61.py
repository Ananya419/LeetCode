class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[-float('inf')] * 3 for _ in range(n)]
        
        for i in range(m):
            curr_dp = [[-float('inf')] * 3 for _ in range(n)]
            for j in range(n):
                val = coins[i][j]
                
                if i == 0 and j == 0:
                    curr_dp[0][0] = val
                    if val < 0:
                        curr_dp[0][1] = 0
                    continue
                
                for k in range(3):
                    best_prev = -float('inf')
                    if i > 0:
                        best_prev = max(best_prev, dp[j][k])
                    if j > 0:
                        best_prev = max(best_prev, curr_dp[j-1][k])
                        
                    if best_prev != -float('inf'):
                        curr_dp[j][k] = max(curr_dp[j][k], best_prev + val)
                    
                    if k > 0 and val < 0:
                        best_prev_k_minus_1 = -float('inf')
                        if i > 0:
                            best_prev_k_minus_1 = max(best_prev_k_minus_1, dp[j][k-1])
                        if j > 0:
                            best_prev_k_minus_1 = max(best_prev_k_minus_1, curr_dp[j-1][k-1])
                            
                        if best_prev_k_minus_1 != -float('inf'):
                            curr_dp[j][k] = max(curr_dp[j][k], best_prev_k_minus_1)
            dp = curr_dp
            
        return max(dp[n-1])


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    coins = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    print(sol.maximumAmount(coins))  # Output: 17