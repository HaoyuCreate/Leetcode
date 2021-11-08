class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, item in enumerate(s):
            if item not in dic.keys():
                dic[item] = []
            dic[item].append(i)

        first = len(s)
        for key in dic.keys():
            if len(dic[key]) == 1:
                first = min(first, dic[key][0])
        first = -1 if first == len(s) else first
        return first