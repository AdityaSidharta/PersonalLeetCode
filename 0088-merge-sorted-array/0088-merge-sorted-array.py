class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n == 0:
            return
        else:
            pm = m - 1
            pn = n - 1
            pr = m + n - 1
            while pr >= 0:
                if pm < 0:
                    nums1[pr] = nums2[pn]
                    pr = pr - 1
                    pn = pn - 1
                elif pn < 0:
                    nums1[pr] = nums1[pm]
                    pr = pr - 1
                    pm = pm - 1
                else:
                    if nums1[pm] >= nums2[pn]:
                        nums1[pr] = nums1[pm]
                        pr = pr - 1
                        pm = pm - 1
                    else:
                        nums1[pr] = nums2[pn]
                        pr = pr - 1
                        pn = pn - 1