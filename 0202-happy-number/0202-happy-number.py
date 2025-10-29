class Solution:
    def get_happy_sum(self, number):
        happy_sum = 0
        current = number % 10
        remainder = number // 10
        print(current, remainder)
        while remainder != 0:
            happy_sum = happy_sum + current ** 2
            current = remainder % 10
            remainder = remainder // 10
            print(current, remainder)
        return happy_sum + current ** 2

    def isHappy(self, n: int) -> bool:
        previous_seen = set()
        n = self.get_happy_sum(n)
        
        while n not in previous_seen and n != 1:
            previous_seen.add(n)
            n = self.get_happy_sum(n)
        
        return n == 1