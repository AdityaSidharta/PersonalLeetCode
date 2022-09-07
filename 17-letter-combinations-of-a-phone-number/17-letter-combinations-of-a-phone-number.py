class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapper = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
        def dp(phoneNumber, current, results):
            if len(phoneNumber) == 0:
                results.append(''.join(current))
            else:
                firstDigit = phoneNumber[0]
                restDigits = phoneNumber[1:]
                if firstDigit == "0":
                    dp(restDigits, current + ['0'], results)
                elif firstDigit == "1":
                    dp(restDigits, current + ['1'], results)
                else:
                    letters = mapper[firstDigit]
                    for letter in letters:
                        dp(restDigits, current + [letter], results)
        if digits == "":
            return []
        else:
            results = []
            dp(digits, [], results)
            return results