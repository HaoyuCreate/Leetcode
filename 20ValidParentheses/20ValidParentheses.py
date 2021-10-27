class Solution:
    def isValid(self, s: str) -> bool:
        # stack for "("
        stack1 = []
        # stack for "["
        stack2 = []
        # stack for "{"
        stack3 = []

        for chr in list(s):
            if chr == '(' or chr == ')':
                top = stack1.pop() if len(stack1)>0 else 0
                val = -1 if chr == '(' else 1
                if top + val != 0:
                    stack1.extend([top,val])

            if chr == '[' or chr == ']':
                top = stack2.pop() if len(stack2)>0 else 0
                val = -1 if chr == '[' else 1
                if top + val != 0:
                    stack2.extend([top,val])

            if chr == '{' or chr == '}':
                top = stack3.pop() if len(stack3) > 0 else 0
                val = -1 if chr == '[' else 1
                if top + val != 0:
                    stack3.extend([top, val])

        return (sum(stack1) == 0 and sum(stack2) == 0 and sum(stack3) == 0)


if __name__ == '__main__':
    solution = Solution()
    s = "([)]"
    print(solution.isValid(s))