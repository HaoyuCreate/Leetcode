class Solution:
    def generate(self, numRows: int):
        root = [1]
        result = []
        for i in range(numRows):
            # insert 0 into the list at head and tail
            result.append(root)
            curr_row = root.copy()
            root = []
            curr_row.insert(0,0)
            curr_row.insert(len(curr_row),0)
            for k in range(len(curr_row)-1):
                root.append(curr_row[k]+curr_row[k+1])

        return result

if __name__=='__main__':
    solution = Solution()
    print(solution.generate(3))

