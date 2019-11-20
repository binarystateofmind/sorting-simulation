
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np

import bubblesort
import insertionsort
import selectionsort
import quicksort
import mergesort

import tkinter
    
if __name__ == "__main__":

    # manual testing #######################################################
    # arr = list(range(30))

    arr = np.random.lognormal(3., 1., 30)

    # random.seed(time.time())
    # random.shuffle(arr)

    selectionSort = selectionsort.SelectionSort()
    insertionSort = insertionsort.InsertionSort()
    bubbleSort = bubblesort.BubbleSort()
    mergeSort = mergesort.MergeSort()
    quickSort = quicksort.QuickSort()

    # fig, axs = plt.subplots(figsize=[9,6], sharey=True) # for a single technique
    # vis = quickSort.getAnimation(s.copy(), fig, axs)


    fig, (axs, axs2, axs3, axs4, axs5) = plt.subplots(1, 5, figsize=[20,6], sharey=True)  # for all the sorting techniques
    visualization = selectionSort.getAnimation(arr.copy(), fig, axs) 
    visualization2 = insertionSort.getAnimation(arr.copy(), fig, axs2) 
    visualization3 = bubbleSort.getAnimation(arr.copy(), fig, axs3) 
    visualization4 = mergeSort.getAnimation(arr.copy(), fig, axs4) 
    visualization5 = quickSort.getAnimation(arr.copy(), fig, axs5) 


    plt.show()
    ##################################################################################

    # size = int(input("Enter the size of your array: "))
    # arr = list(range(size))

    # dtype = int(input("Select data type (1. Random, 2. Almost sorted, 3. Synthetic): "))
    # if dtype == 1:
    #     random.seed(time.time())
    #     random.shuffle(arr)
    # elif dtype == 2:
    #     print("Not implemented")
    #     #TODO
    # elif dtype == 3:
    #     print("Not implemented")
    #     #TODO

    # method = int(input("Select sorting algorithm (1: Bubble, 2: Selection, 3: Insertion, 4: Merge, 5: Quick): "))
    # if method == 1:
    #     bubbleSort = bubblesort.BubbleSort()
    #     generator = bubbleSort.visualSort(arr)
    #     title = "Bubble Sort"
    # elif method  == 2:
    #     selectionSort = selectionsort.SelectionSort()
    #     generator = selectionSort.visualSort(arr)
    #     update_func = selectionSort.update_func
    #     title = "Selection Sort"
    # elif method  == 3:    
    #     insertionSort = insertionsort.InsertionSort()
    #     generator = insertionSort.visualSort(arr)
    #     title = "Insertion Sort"
    # elif method  == 4:    
    #     mergeSort = mergesort.MergeSort()
    #     generator = mergeSort.visualMergesort(arr, 0, len(arr) - 1)
    #     title = "Merge Sort"
    # elif method  == 5:       
    #     quickSort = quicksort.QuickSort()
    #     generator = quickSort.visualSort(arr, 0, len(arr) - 1)
    #     title = "Quick Sort"

    # fig, (bsAxes, ssAxes, isAxes, msAxes, qsAxes) = plt.subplots(1, 5, sharex=True, sharey=True, figsize=[16,6])

    # plt.show()

