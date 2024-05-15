class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        start = 0
        max_length = 0
        char_count = collections.defaultdict(int)
        
        for end in range(len(s)):
            char_count[s[end]] += 1
            max_freq = max(max_freq, char_count[s[end]])
            
            if end - start + 1 - max_freq > k:
                char_count[s[start]] -= 1
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length
