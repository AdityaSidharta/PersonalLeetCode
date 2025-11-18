class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        current = nums[0]
        best_solution = 10e9
        if current >= target:
            best_solution = min(right - left + 1, best_solution)
        while right <= len(nums) - 2:
            if current >= target:
                best_solution = min(right - left + 1, best_solution)
            right = right + 1
            current = current + nums[right]
            if current >= target:
                best_solution = min(right - left + 1, best_solution)
            while current > target:
                best_solution = min(right - left + 1, best_solution)
                current = current - nums[left]
                left = left + 1
            if current >= target:
                best_solution = min(right - left + 1, best_solution)
        return best_solution if best_solution < 10e9 else 0