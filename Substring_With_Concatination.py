class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = {}
        
        # Build frequency map of words
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
        res = []
        
        # Try each offset
        for i in range(word_len):
            left = i
            seen = {}
            count = 0
            
            # Slide window
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j+word_len]
                
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    
                    # Too many occurrences → shrink
                    while seen[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # Valid window
                    if count == len(words):
                        res.append(left)
                else:
                    # Reset window
                    seen.clear()
                    count = 0
                    left = j + word_len
        
        return res
    
# Example below:
if __name__ == "__main__":
    sol = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(f"Starting indices of substring concatenation: {sol.findSubstring(s, words)}")