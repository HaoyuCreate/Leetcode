class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        h = len(mat)
        w = len(mat[0])
        if r * c != w * h:
            return mat
        temp = []
        for i in range(h):
            temp.extend(mat[i])

        result = []
        curr_row = []
        for k in range(len(temp)):
            if len(curr_row) < c:
                curr_row.append(temp[k])
                print(curr_row)
            else:
                result.append(curr_row)
                curr_row = []
                curr_row.append(temp[k])
        result.append(curr_row)
        return result

    def matrixReshape2(self, mat, r: int, c: int):
        h = len(mat)
        w = len(mat[0])
        if r * c != w * h:
            return mat

        result = []
        curr_row = []
        for i in range(h):
            for j in range(w):
                temp = mat[i][j]
                if len(curr_row) < c:
                    curr_row.append(temp)
                else:
                    result.append(curr_row)
                    curr_row = []
                    curr_row.append(temp)
        result.append(curr_row)
        return result


if __name__=='__main__':
    solution = Solution()

    mat = [[1,2],[3,4]]
    r = 2
    c = 2

    print(solution.matrixReshape2(mat,r,c))
