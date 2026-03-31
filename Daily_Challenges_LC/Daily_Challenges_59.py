class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1
        ans = ['?'] * L
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if ans[i+j] != '?' and ans[i+j] != str2[j]:
                        return ""
                    ans[i+j] = str2[j]
                    
        q_count = [0] * n
        mismatch_count = [0] * n
        
        for i in range(n):
            if str1[i] == 'F':
                qc = 0
                mc = 0
                for j in range(m):
                    if ans[i+j] == '?':
                        qc += 1
                    elif ans[i+j] != str2[j]:
                        mc += 1
                
                if qc == 0 and mc == 0:
                    return ""
                
                q_count[i] = qc
                mismatch_count[i] = mc

        for k in range(L):
            if ans[k] != '?':
                continue
                
            forbidden = set()
            start_i = max(0, k - m + 1)
            end_i = min(n - 1, k)
            
            for i in range(start_i, end_i + 1):
                if str1[i] == 'F':
                    if q_count[i] == 1 and mismatch_count[i] == 0:
                        forbidden.add(str2[k - i])
                        
            chosen = None
            for char_code in range(97, 123):
                c = chr(char_code)
                if c not in forbidden:
                    chosen = c
                    break
            
            if chosen is None:
                return ""
                
            ans[k] = chosen
            
            for i in range(start_i, end_i + 1):
                if str1[i] == 'F':
                    q_count[i] -= 1
                    if str2[k - i] != chosen:
                        mismatch_count[i] += 1
                        
        return "".join(ans)


# Example Usage:
sol = Solution()
print(sol.generateString("FTF", "abc"))  # Output: "aabc"
