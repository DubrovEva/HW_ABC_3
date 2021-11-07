# HW_ABC_3
Домашнее задание номер 3 по курсу "Архитектура вычислительных систем"

# Отчет по заданию 3

## Описание полученного задания
**Обобщенный артефакт, используемый в задании:** Квадратные матрицы с действительными числами

**Базовые альтернативы
(уникальные параметры,
задающие отличительные
признаки альтернатив):**
1. Обычный двумерный
массив
2. Диагональная (на основе
одномерного массива)
3. Нижняя треугольная
матрица (одномерный массив с формулой пересчета)

**Общие для всех альтернатив переменные:** Размерность – целое число

**Общие для всех альтернатив функции:** Вычисление среднего арифметического (действительное число)

**Обработка контейнера:** Упорядочить элементы контейнера по возрастанию используя сортировку с помощью прямого включения (Straight Insertion). В качестве ключей для сортировки и других действий используются результаты функции, общей для всех альтернатив.

## Характеристики программы
**Число модулей**: 6

**Результаты тестирования:**
1. test_for_all_types_of_square_matrix - (real) 0.0018s, (user) 0.0018s, (sys) 0.000s
2. test_for_diagonal_matrix - (real) 0.018s, (user) 0.014s, (sys) 0.004s
3. test_for_lower_triangular_matrix - (real) 0.0019s, (user) 0.015s, (sys) 0.004s
4. test_for_reqular_array - (real) 0.018s, (user) 0.015s, (sys) 0.004s
5. big_test_for_all_types - (real) 0.043s, (user) 0.035s, (sys) 0.009s

## Особенности архитектуры программы

**Отображение содержимого модуля main на память

* main
  * ifile (file)
  * str (string)
  * values (list)
  * container (module) 
  * ofile (file) 
  * container.py (module) 
  * inputFileName (string)
  * outputFileName (string)

**Отображение содержимого модуля conteiner на память**

* container.py
  * store (list)
* ReadStrArray
  * arrayLen (int)
  * i (int)
  * key (int)
  * n (int0
  * matrix_values (list)
* Print
  * matrix (module)
* Write
  * matrix (module)
* Sort
  * i (int)
  * index (int)

**Отображение модуля RegularArray на память**

* RegularArray
  * n (int)
  * values (list)
* ReadSquareMatrix
  * n (int)
  * values (list)
* Print
  * i (int)
  * j (int)
* Write
  * str_values (list)
* Average

**Отображение модуля DiagonalMatrix на память**

* DiagonalMatrix
  * n (int)
  * list (values)
* ReadSquareMatrix
  * n (int)
  * values (list)
* Print
  * i (int)
  * j (int)
* Write
  * description
* Average

**Отображение модуля LowerTriangularMatrix на память**

* LowerTriangularMatrix
  * n (int)
  * values (list)
* ReadSquareMatrix
  * n (int)
  * values (list)
  * i (int)
  * j (int)
* Print
  * index (int)
  * i (int)
  * j (int)
* Write
  * index (int)
  * description (string)
* Average

**Отображение модуля SquareMatrix на память**

* SquareMatrix
* ReadSquareMatrix
* Print
* Write
* Average
