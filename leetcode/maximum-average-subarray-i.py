class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_average = window_sum / k

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_average = max(max_average, window_sum / k)

        return max_average
