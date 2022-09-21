from random import choice

'''
1,2,3,6,4,5

LOW = 0
HIGH = 1
K = 5
PIVOT = 0
LEFT = 1
HIGH = 1
'''




class Solution:
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]
    
    def quickSelect(self, nums, low, high, k):      
        if low == high:
            assert low == k
            return nums[k]
        pivot = low
        left = low + 1
        right = high
        while right - left > 0:
            if nums[pivot] > nums[left]:
                left = left + 1
            else:
                self.swap(nums, left, right)
                right = right - 1
        if nums[pivot] <= nums[left]:
            self.swap(nums, pivot, left - 1)
            pivot = left - 1
        else:
            self.swap(nums, pivot, left)
            pivot = left
        if k == pivot:
            return nums[pivot]
        elif k < pivot:
            return self.quickSelect(nums, low, pivot - 1, k)
        else:
            return self.quickSelect(nums, pivot + 1, high, k)        
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return None
        if k <= 0:
            raise ValueError("k is too small")
        if len(nums) < (k):
            raise ValueError("k is too large")
        if len(nums) == 1:
            return nums[0]
        else:
            return self.quickSelect(nums, 0, len(nums)-1, len(nums) - k)