class Solution:
    def transposeDiag(self, matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        return matrix

    def transposeReverseDiag(self,matrix):
        h = len(matrix)
        w = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(w-i):
                matrix[i][j],matrix[w-1-j][h-1-i] = matrix[w-1-j][h-1-i],matrix[i][j]
        return matrix

    def verticalReverser(self, matrix):
        h = len(matrix)

        for i in range(h/2):
            for j in range(len(matrix[0])):
                matrix[i][j],matrix[h-1-i][j] = matrix[h-1-i][j],matrix[i][j]
        return matrix


    def horizentalReverse(self, matrix):
        w = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(int(w / 2)):
                matrix[i][j], matrix[i][w - 1 - j] = matrix[i][w - 1 - j], matrix[i][j]
        return matrix

    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = self.transposeDiag(matrix)
        matrix = self.horizentalReverse(matrix)
        return matrix