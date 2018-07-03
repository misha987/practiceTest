import numpy
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)

try:
    file = open('myFile.txt')
except IOError as error:
    print('Error')
else:
    data = []
    v1 = []
    i = 0
    nextElem = file.readline()
    while len(nextElem) != 0:
        tmpStr = '';
        tmpArr = []
        tmpFree = []
        prevSymb = ' '
        if len(nextElem) != 0:
            for j in nextElem:
                if j in '1234567890.-': # если символ - цифра, то собираем число
                    tmpStr += j
                elif j == 'x':
                    prevSymb = 'x'
                    tmpArr.append(float(tmpStr))
                    tmpStr = ''
                elif j in '=':
                    tmpStr = ''
            data.append(tmpArr)
            v1.append(float(tmpStr))
        nextElem = file.readline()
    try:
        k = numpy.linalg.solve(data, v1)
        print(k)
        logging.info("\nlevelname: INF message: CoefficientsOfX: %s freeCoefficients: %s, result: %s" % (data, v1, k))
    except numpy.linalg.LinAlgError:
        print("Нельзя посчитать")
    file.close()
