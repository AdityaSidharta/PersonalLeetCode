class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        pivot = (left + right) // 2 if left != 0 else ((left + right) // 2) + ((left + right) % 2)
        while (left <= right) and (1 <= pivot <= len(arr) - 2):
            if (arr[pivot - 1] < arr[pivot]) and (arr[pivot] > arr[pivot + 1]):
                return pivot
            elif (arr[pivot - 1] < arr[pivot]) and (arr[pivot] < arr[pivot + 1]):
                left = pivot + 1
                pivot = (left + right) // 2 if left != 0 else ((left + right) // 2) + ((left + right) % 2)
            else:
                assert (arr[pivot - 1] > arr[pivot]) and (arr[pivot] > arr[pivot + 1])
                right = pivot - 1
                pivot = (left + right) // 2 if left != 0 else ((left + right) // 2) + ((left + right) % 2)
        return -1