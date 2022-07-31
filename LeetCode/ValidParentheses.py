# https://leetcode.com/problems/valid-parentheses/

def is_opening(p):
    return p == '(' or p == '{' or p == '['
    
    
def same_kind(p, m):
    if p == '(' and m == ')':
        return True
    if p == '{' and m == '}':
        return True
    if p == '[' and m == ']':
        return True
    return False

    
class Solution: 
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if(is_opening(c)):
                stack.append(c)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if not same_kind(temp,c):
                    return False
        if not stack:
            return True
        else:
            return False
    