from squarematrix import SquareMatrix

# ------------------------------------------------------------------------------
# regulararray.py - содержит функции обработки обычного квадратного массива чисел
# ------------------------------------------------------------------------------


class RegularArray(SquareMatrix):
    def __init__(self):
        self.n = 0
        self.values = []

    # Ввод параметров обычного квадратного массива из потока
    def ReadSquareMatrix(self, n, values):
        # должно быт как минимум три непрочитанных значения в массиве
        self.n = n
        self.values = list(map(float, values))

    # Вывод параметров обычного квадратного массива
    def Print(self):
        print("Regular array: n = ", self.n)
        print("Values:")
        for i in range(self.n):
            print("  ", end="")
            for j in range(self.n):
                print(self.values[self.n*i+j], end=" ")
            print()

    # Вывод параметров обычного квадратного массива в поток
    def Write(self, ostream):
        str_values = list(map(str, self.values))
        str_values = "\n".join([" ".join(str_values[i * self.n:(i + 1) * self.n]) for i in range(self.n)])
        ostream.write("Regular array: n = {}\nValue:\n{}\n"
                      "Average = {}".format(self.n, str_values, self.Average()))

    # Вычисление среднего арифметического значений обычного квадратного массива чисел
    def Average(self):
        return sum(self.values)/self.n/self.n
