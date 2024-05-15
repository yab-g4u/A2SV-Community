class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        res = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                idx = stack.pop()
                left = idx - stack[-1] if stack else idx + 1
                right = i - idx
                res += arr[idx] * left * right
                res %= MOD
            stack.append(i)

        return res
