from collections import deque

'''
 0123456789012
"lee(t(c)o)de)"

 TTTTTTTTTTTTF
 
 queue = [3,]
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == '':
            return ''
        else:
            keep = []
            for idx in range(len(s)):
                if s[idx] == '(' or s[idx] == ')':
                    keep.append(False)
                else:
                    keep.append(True)
            stack = deque()
            for idx in range(len(s)):
                if s[idx] == '(':
                    stack.append(idx)
                elif s[idx] == ')':
                    if len(stack):
                        open_idx = stack.pop()
                        keep[idx] = True
                        keep[open_idx] = True
            result = []
            for idx in range(len(s)):
                if keep[idx]:
                    result.append(s[idx])
            return result
