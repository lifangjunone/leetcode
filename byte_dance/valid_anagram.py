from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        return Counter(s) == Counter(t)

    def isAnagram3(self, s, t):
        mapping = {}
        mapping2 = {}
        for i in s:
            mapping[i] = mapping.get(i, 0) + 1
        for j in t:
            mapping2[j] = mapping2.get(j, 0) + 1
        return mapping == mapping2

    def isAnagram4(self, s, t):
        p1 = {}
        p2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            p1[s[i]] = p1.get(s[i], 0) + 1
            p2[t[i]] = p2.get(t[i], 0) + 1
        return p1 == p2

    def isAnagram5(self, s, t):
        m1, m2 = [0]*26, [0]*26
        if len(s) != len(t): return False
        for i in s:
            m1[ord(i) - ord('a')] += 1
            m2[ord(i) - ord('a')] += 1
        return m1 == m2
