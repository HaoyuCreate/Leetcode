class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        maxn = 0

        for char in s:
            if char == '(':
                left += 1
            if char == ')':
                right += 1
            if left - right == 0:
                maxn = max(maxn, 2 * right)
            if left - right < 0:
                left = right = 0

        left = right = 0
        for char in reversed(s):
            if char == '(':
                left += 1
            if char == ')':
                right += 1

            if right - left == 0:
                maxn = max(maxn, 2 * left)
            if left > right:
                left = right = 0
        return maxn

