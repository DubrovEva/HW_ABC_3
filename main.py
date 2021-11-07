import sys
from container import *

if __name__ == '__main__':
    if len(sys.argv) == 3:
        inputFileName  = sys.argv[1]
        outputFileName = sys.argv[2]
    elif len(sys.argv) == 2:
        inputFileName  = sys.argv[1]
        outputFileName = "output.txt"
    elif len(sys.argv) == 1:
        print("Incorrect command line! You must write: python main <inputFileName> [<outputFileName>]")
        exit()

    # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
    ifile = open(inputFileName)
    str = ifile.read()
    ifile.close()

    # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
    values = str.replace("\n", " ").split(" ")

    print('Start ==>')

    container = Container()
    figNum = container.ReadStrArray(values)
    container.Sort()

    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    ofile.close()

    print('==> Finish')
