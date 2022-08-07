# https://leetcode.com/problems/maximum-score-from-removing-stones/

def two_empty(a, b, c):
    return ((a == 0) + (b == 0) + (c == 0)) > 1


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        score = 0
        s = [a, b, c]
        while not two_empty(s[0], s[1], s[2]):
            s.sort(reverse=True)
            if s[2] == 0:
                score += min(s[0], s[1])
                break
            s[0] -= 1
            s[1] -= 1
            score += 1
        return score
            