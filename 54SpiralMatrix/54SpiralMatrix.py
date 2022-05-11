class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total_len = len(matrix) * len(matrix[0])

        b_left = 0
        b_right = len(matrix[0])
        b_top = 0
        b_bottom = len(matrix)
        r = c = 0
        result = []
        path = 0

        while path < total_len:
            # move left -> right:
            while c < b_right:
                curr = matrix[r][c]
                result.append(curr)
                path += 1
                c += 1
                if path >= total_len:
                    break
            c -= 1
            b_top += 1
            r += 1
            if path >= total_len:
                break

            # move top -> bottom
            while r < b_bottom:
                curr = matrix[r][c]
                result.append(curr)
                path += 1
                r += 1
                if path >= total_len:
                    break
            r -= 1
            b_right -= 1
            c -= 1
            if path >= total_len:
                break

            # move right -> left
            while c >= b_left:
                curr = matrix[r][c]
                result.append(curr)
                path += 1
                c -= 1
                if path >= total_len:
                    break
            c += 1
            b_left += 1
            r -= 1
            if path >= total_len:
                break

            # move bottom -> top
            while r >= b_top:
                curr = matrix[r][c]
                result.append(curr)
                path += 1
                r -= 1
                if path >= total_len:
                    break
            r += 1
            b_bottom -= 1
            c += 1
            if path >= total_len:
                break

        return result
