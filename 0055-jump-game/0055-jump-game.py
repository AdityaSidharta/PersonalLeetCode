class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            current_maximum = 0
            current_index = 0
            while current_maximum >= current_index and current_index < len(nums):
                if current_index + nums[current_index] > current_maximum:
                    current_maximum = current_index + nums[current_index]
                current_index = current_index + 1
            return current_maximum >= len(nums) - 1