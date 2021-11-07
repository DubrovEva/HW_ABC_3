# ------------------------------------------------------------------------------
# container.h - содержит тип данных, представляющий простейший контейнер
# ------------------------------------------------------------------------------
from squarematrix    import *
from diagonalmatrix import DiagonalMatrix
from regulararray import RegularArray
from lowertriangularmatrix import LowerTriangularMatrix

class Container:
    def __init__(self):
        self.store = []

    # Ввод содержимого контейнера из указанного потока
    def ReadStrArray(self, values):
        arrayLen = len(values)
        i = 0  # Индекс, задающий текущий элемент в массиве
        while i < arrayLen:
            key = int(values[i])
            n = int(values[i + 1])
            matrix_values = values[i + 2:i + 2 + n * n]
            i += n * n + 2
            if key == 1:  # матрица обычнач
                matrix = RegularArray()
            elif key == 2:  # матрица диагональна
                matrix = DiagonalMatrix()
            else:  # матрица нижняя треугольная
                matrix = LowerTriangularMatrix()
            matrix.ReadSquareMatrix(n, matrix_values)
            self.store.append(matrix)

    # Вывод содержимого контейнера
    def Print(self):
        print("Container is store", len(self.store), "matricies:")
        for shape in self.store:
            shape.Print()

    # Вывод содержимого контейнера в указанный поток
    def Write(self, ostream):
        ostream.write("Container is store {} shapes:\n".format(len(self.store)))
        for matrix in self.store:
            matrix.Write(ostream)
            ostream.write("\n")

    # Сортировка контейнера по возрастанию среднего арифметического методом прямого включения
    def Sort(self):
        for i in range(len(self.store)):
            # Считаем, что все предыдущие элементы расположены в порядке возрастания
            #  Тогда первый неотсортированный элемент имеет индекс i
            index = i;
            # Найдем место для неотсортированного элемента
            while index > 0 and self.store[index].Average() < self.store[index - 1].Average():
                self.store[index], self.store[index - 1] = self.store[index - 1], self.store[index]
                index -= 1

