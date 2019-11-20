
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

    selectionSort = selectionsort.SelectionSort()
    insertionSort = insertionsort.InsertionSort()
    bubbleSort = bubblesort.BubbleSort()
    mergeSort = mergesort.MergeSort()
    quickSort = quicksort.QuickSort()

    size = int(input("Enter the size of your array: "))
    arr = list(range(size))

    dtype = int(input("Select data type (1. Random, 2. Almost sorted, 3. Log Synthetic): "))
    if dtype == 1:
        random.seed(time.time())
        random.shuffle(arr)
    elif dtype == 2:
        temp = arr[20]
        arr[20] = arr[19]
        arr[19] = temp
    elif dtype == 3:
        arr = np.random.lognormal(3., 1., size)

    method = int(input("Select sorting algorithm (1: Bubble, 2: Selection, 3: Insertion, 4: Merge, 5: Quick, 6: All of them): "))
    if method == 1:
        fig, axs = plt.subplots(figsize=[9,6])
        anim = bubbleSort.getAnimation(arr, fig, axs)
    elif method  == 2:
        fig, axs = plt.subplots(figsize=[9,6])
        anim = selectionSort.getAnimation(arr, fig, axs)
    elif method  == 3:
        fig, axs = plt.subplots(figsize=[9,6])
        anim = insertionSort.getAnimation(arr, fig, axs)
    elif method  == 4:  
        fig, axs = plt.subplots(figsize=[9,6]) 
        anim = mergeSort.getAnimation(arr, fig, axs)
    elif method  == 5: 
        fig, axs = plt.subplots(figsize=[9,6])     
        anim = quickSort.getAnimation(arr, fig, axs)
    elif method == 6:
        fig, (axs1, axs2, axs3, axs4, axs5) = plt.subplots(1, 5, sharey=True, figsize=[20,6])
        anim1 = bubbleSort.getAnimation(arr.copy(), fig, axs1)
        anim2 = selectionSort.getAnimation(arr.copy(), fig, axs2)
        anim3 = insertionSort.getAnimation(arr.copy(), fig, axs3)
        anim4 = mergeSort.getAnimation(arr.copy(), fig, axs4)
        anim5 = quickSort.getAnimation(arr.copy(), fig, axs5)

    plt.show()
