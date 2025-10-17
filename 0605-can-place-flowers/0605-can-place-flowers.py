class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        idx = 0
        total = len(flowerbed)
        while idx < total and n != 0:
            #process
            if idx == 0 and idx == total-1:
                if flowerbed[idx] == 0:
                    flowerbed[idx] = 1
                    n = n - 1
            elif idx == 0:
                if flowerbed[idx] == 0 and flowerbed[idx+1] == 0:
                    flowerbed[idx] = 1
                    n = n - 1
            elif idx == total-1:
                if flowerbed[idx] == 0 and flowerbed[idx-1] == 0:
                    flowerbed[idx] = 1
                    n = n - 1
            else:
                if flowerbed[idx] == 0 and flowerbed[idx+1] == 0 and flowerbed[idx-1] == 0:
                    flowerbed[idx] = 1
                    n = n - 1
            idx = idx + 1
        return n == 0
            