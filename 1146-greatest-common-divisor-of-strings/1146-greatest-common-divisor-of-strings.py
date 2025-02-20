class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == "" or str2 == "":
            return ""

        str1_len = len(str1)
        str2_len = len(str2)

        word_len = min(str1_len, str2_len)
        common_string = ""
        for idx in range(word_len):
            if str1[:idx+1] == str2[:idx+1]:
                common_string = str1[:idx+1]
        
        common_string_len = len(common_string)
        result = ""
        for idx in range(word_len):
            if str1_len % (idx + 1) == 0 and str2_len % (idx + 1) == 0:
                if str1 == (common_string[:idx + 1] * (str1_len // (idx + 1))) and  str2 == (common_string[:idx + 1] * (str2_len // (idx + 1))):
                    result =  common_string[:idx + 1]
        return result
        