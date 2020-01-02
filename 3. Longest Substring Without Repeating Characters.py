# 3 Longest Substring Without Repeating Characters  
class lengthOfLongestSubstring(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = []  # memory for storing characters
        l = 0   # the longest length ever
        for c in s:
            if c in m:
                l = max(l, len(m))
                m = m[m.index(c)+1:]
            m.append(c)
        return max(l, len(m))
