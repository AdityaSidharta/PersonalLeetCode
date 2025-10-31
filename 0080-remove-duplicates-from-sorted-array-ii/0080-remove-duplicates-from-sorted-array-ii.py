class Solution:
    def getnext(self, nums, i, is_dunder):
        while i < len(nums):
            if is_dunder :
                if nums[i] == 9999999:
                    return i
            else:
                if nums[i] != 9999999:
                    return i
            i = i + 1
        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        prev = -9999999
        prevprev = -9999999
        for i in range(len(nums)):
            if nums[i] == prev and nums[i] == prevprev:
                nums[i] = 9999999
            else:
                prevprev = prev
                prev = nums[i]
        number_pointer = 0
        dunder_pointer = 0
        stay = False
        while True:
            number_pointer = self.getnext(nums, number_pointer, False)
            if number_pointer == len(nums):
                break

            dunder_pointer = self.getnext(nums, dunder_pointer , True)
            if dunder_pointer == len(nums):
                break
            print(number_pointer, dunder_pointer)
            if dunder_pointer < number_pointer:
                print("here")
                nums[dunder_pointer], nums[number_pointer] = nums[number_pointer], nums[dunder_pointer]
                dunder_pointer = dunder_pointer + 1
            else:
                number_pointer = number_pointer + 1

        output = 0
        for num in nums:
            if num != 9999999:
                output = output + 1
        return output