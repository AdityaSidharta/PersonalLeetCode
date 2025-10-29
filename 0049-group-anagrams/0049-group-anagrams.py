class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        else:
            sorted_strs = [None] * len(strs)
            for i in range(len(strs)):
                sorted_strs[i] = ''.join(sorted(strs[i]))
            print(strs)
            print(sorted_strs)
            seen = {}
            for i in range(len(sorted_strs)):
                if sorted_strs[i] in seen:
                    seen[sorted_strs[i]].append(i)
                else:
                    seen[sorted_strs[i]] = [i]
            result = []
            for _, indices in seen.items():
                mini_result = []
                for index in indices:
                    mini_result.append(strs[index])
                result.append(mini_result)
            return result
