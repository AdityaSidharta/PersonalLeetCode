class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        counter = 0
        for num in nums:
            if counter <= 0:
                candidate = num
                counter = 1
            else:
                if candidate == num:
                    counter = counter + 1
                else:
                    counter = counter - 1
        return candidate