from matplotlib import pyplot
from functools import partial
import timeit
import random
import numpy

from bubblesort import bubblesort
from quicksort import quicksortstarter
from mergesort import mergesort
from selectionsort import selectionsort
from insertionsort import insertionsort


def test(arr):
    return 0


def plotTC(fn, nTests):
    x = []
    y = []
    arr = []
    for j in range(0, 25):
        arr.append(j)

    arr.reverse()
    for i in range(0, nTests):
        arr2 = arr.copy()
        testNTimer = timeit.Timer(partial(fn, arr2))
        t = testNTimer.timeit(number=1)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')


def main():
    with open('data/guids.txt') as dataFile:
        lines = dataFile.readlines()

    for i in range(1, 6):
        arr1 = lines[0:5000]

        testNTimer = timeit.Timer(partial(bubblesort, arr1))
        t = testNTimer.timeit(number=1)

        print('time = '+str(t))
    # print(arr1)

    # read in data files
    # format data into sortable ready form

    # do every sort on each set of data, returning and collecting runtime and space used for each run

    # use output to create 16 graphs

    # 2 different y-axis, runtime and space used
    # 2 different x-axis, data size and data sortedness
    # 4 different types of data
    # 2 synthetic distributions
    # bell curve
    # perfect
    # 2 real world data sets
    # zipcodes
    # birthdate

    # plotTC(bubblesort, 50)
    # plotTC(quicksortstarter, 10)
    # plotTC(mergesort, 10)
    # plotTC(insertionsort, 10)
    # plotTC(selectionsort, 10)
    # pyplot.show()

if __name__ == "__main__":
    main()


def produceDataFiles():
    filename = 'data/convertcsv.csv'
    with open(filename) as dataFile:
        lines = dataFile.readlines()

    guid = []
    phones = []
    zip9 = []
    birthday = []

    lineN = 1
    while lineN < len(lines) - 1:
        parts = lines[lineN].split(',')
        guid.append(parts[0])
        phones.append(parts[1])
        zip9.append(parts[2])
        birthday.append(parts[3][0:-1])
        lineN += 1

    filename = 'data/guids.txt'
    with open(filename, 'w') as file_object:
        for line in guid:
            file_object.write(line)
            file_object.write('\n')

    filename = 'data/phonenumbers.txt'
    with open(filename, 'w') as file_object:
        for line in phones:
            file_object.write(line)
            file_object.write('\n')

    filename = 'data/zip9s.txt'
    with open(filename, 'w') as file_object:
        for line in zip9:
            file_object.write(line)
            file_object.write('\n')

    filename = 'data/birthdays.txt'
    with open(filename, 'w') as file_object:
        for line in birthday:
            file_object.write(line)
            file_object.write('\n')