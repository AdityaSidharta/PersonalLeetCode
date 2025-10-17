class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1 if nums[0] != val else 0
        left_index = 0
        right_index = len(nums) - 1
        while left_index != right_index:
            if nums[left_index] != val:
                left_index = left_index + 1
            else:
                if nums[right_index] == val:
                    right_index = right_index - 1
                else:
                    nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
                    left_index = left_index + 1
        if nums[left_index] == val:
            return left_index
        else:
            return left_index + 1