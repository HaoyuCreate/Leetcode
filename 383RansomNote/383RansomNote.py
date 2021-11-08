class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        countR = Counter(ransomNote)
        countM = Counter(magazine)
        for i in ransomNote:
            if countR[i] > countM[i]:
                return False
        return True


if __name__=='__main__':
    solution = Solution()
    ransomNote = "aa"
    magazine = "ab"
    print(solution.canConstruct(ransomNote,magazine))