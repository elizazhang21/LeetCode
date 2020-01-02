# 5. Longest Palindromic Substring 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return s
        
        
        # Manacher's Algorithm
        right = center = 0
        # By adding in filler characters, we're able to detect any even-length palindromes
        temp = s
        s = '#'.join('^{}$'.format(s))
        palinarray = [0] * len(s)
        for i in range(1, len(s) - 1):
            palinarray[i] = (right > i) and min(right - i, palinarray[2*center - i])
            while s[i + 1 + palinarray[i]] == s[i - 1 - palinarray[i]]:
                palinarray[i] += 1
            if i + palinarray[i] > right:
                center, right = i, i + palinarray[i]
        maxLen, centerIndex = max((n, i) for i, n in enumerate(palinarray))
        return temp[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]  