from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        result = []

        for i in range(len(p), len(s)):
            if s_count == p_count:
                result.append(i - len(p))

            s_count[s[i]] += 1
            s_count[s[i - len(p)]] -= 1
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]

        if s_count == p_count:
            result.append(len(s) - len(p))

        return result
