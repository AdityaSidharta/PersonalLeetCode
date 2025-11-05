class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            if i == 0:
                counter = counter + 1
            else:
                if nums[i] != nums[i-1]:
                    nums[counter] = nums[i]
                    counter = counter + 1
        return counter