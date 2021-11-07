from squarematrix import SquareMatrix

# ------------------------------------------------------------------------------
# diagonalmatrix.py - содержит функции обработки диагональной матрицы
# ------------------------------------------------------------------------------

class DiagonalMatrix(SquareMatrix):
    def __init__(self):
        self.n = 0
        self.values = []

    # Ввод параметров диагональной матрицы из потока
    def ReadSquareMatrix(self, n, values):
        self.n = n
        values = list(map(float, values))
        self.values = [values[n*i + i] for i in range(self.n)]

    # Вывод параметров диагональной матрицы
    def Print(self):
        print("Diagonal matrix: n = ", self.n)
        print("Values:")
        for i in range(self.n):
            print("  ", end=" ")
            for j in range(self.n):
                if i == j:
                    print(self.values[i], end=" ")
                else:
                    print(0, end=" ")
            print()

    # Вывод параметров диагональной матрицы в поток
    def Write(self, ostream):
        description = "Diagonal matrix: n = " + str(self.n) + "\nValue:\n"
        for i in range(self.n):
            description += "  "
            for j in range(self.n):
                if i == j:
                    description += str(self.values[i]) + " "
                else:
                    description += "0 "
            description += "\n"
        description += "Average = " + str(self.Average())
        ostream.write(description)

    # Вычисление среднего арифметического значений диагональной матрицы
    def Average(self):
        return sum(self.values) / self.n / self.n
