class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        counter1 = Counter(s)
        counter2 = Counter(t)

        if len(s) == len(t):
            for i in s:
                if counter1[i] != counter2[i]:
                    return False
            return True
        else:
            return False