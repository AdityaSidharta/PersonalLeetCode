class Solution:
    def maxArea(self, height: List[int]) -> int:
        lenh = len(height)
        l = 0
        r = lenh - 1
        max_volume = 0
        while l < r:
            cur_volume = (r-l) * min(height[l], height[r])
            if max_volume < cur_volume:
                max_volume = cur_volume
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return max_volume