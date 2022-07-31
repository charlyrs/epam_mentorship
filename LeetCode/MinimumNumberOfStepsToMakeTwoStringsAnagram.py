# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd = {}
        td = {}
        l = len(s)
        for c in set(s):
            sd[c] = s.count(c)
        for c in set(t):
            td[c] = t.count(c)
       
        count = 0
        for c in sd:
            temp = td.get(c,0)
            if temp != 0:
                if sd[c] - td[c] > 0:
                    count += sd[c] - td[c]
            else:
                count += sd[c]
        return count
        
        