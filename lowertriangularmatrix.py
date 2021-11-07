from squarematrix import SquareMatrix

# ------------------------------------------------------------------------------
# lowertriangularmatrix.py - содержит функции обработки нижней треугольной матрицы
# ------------------------------------------------------------------------------

class LowerTriangularMatrix(SquareMatrix):
    def __init__(self):
        self.n = 0
        self.values = []

    # Ввод параметров нижней треугольной матрицы из потока
    def ReadSquareMatrix(self, n, values):
        self.n = n
        self.values = []
        values = list(map(float, values))
        for i in range(n):
            for j in range(n):
                if j <= i:
                    self.values.append(values[i*n + j])

    # Вывод параметров диагональной матрицы
    def Print(self):
        print("Lower triangular matrix: n = ", self.n)
        print("Values:")
        index = 0
        for i in range(self.n):
            print("  ", end=" ")
            for j in range(self.n):
                if j <= i:
                    print(self.values[index], end=" ")
                    index += 1
                else:
                    print(0, end=" ")
            print()

    # Вывод параметров диагональной матрицы в поток
    def Write(self, ostream):
        description = "Lower triangular matrix: n = " + str(self.n) + "\nValue:\n"
        index = 0
        for i in range(self.n):
            description += "  "
            for j in range(self.n):
                if j <= i:
                    description += str(self.values[index]) + " "
                    index += 1
                else:
                    description += "0 "
            description += "\n"
        description += "Average = " + str(self.Average())
        ostream.write(description)

    # Вычисление среднего арифметического значений диагональной матрицы
    def Average(self):
        return sum(self.values) / self.n / self.n
