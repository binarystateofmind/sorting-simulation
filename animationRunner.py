
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

import bubblesort
import insertionsort
import selectionsort
import quicksort
import mergesort
    
if __name__ == "__main__":

    # manual testing #######################################################
    arr = list(range(30))

    random.seed(time.time())
    random.shuffle(arr)

    selectionSort = selectionsort.SelectionSort()
    insertionSort = insertionsort.InsertionSort()
    bubbleSort = bubblesort.BubbleSort()
    mergeSort = mergesort.MergeSort()
    quickSort = quicksort.QuickSort()

    # fig, axs = plt.subplots(figsize=[9,6], sharey=True)

    # vis = quickSort.getAnimation(arr.copy(), fig, axs)

    # fig, (axs, axs2, axs3) = plt.subplots(1, 3, figsize=[9,6], sharey=True)
    # visualization = bubbleSort.getAnimation(arr.copy(), fig, axs)
    # visualization2 = insertionSort.getAnimation(arr.copy(), fig, axs2)
    # visualization3 = selectionSort.getAnimation(arr.copy(), fig, axs3)

    fig, (axs, axs2, axs3, axs4, axs5) = plt.subplots(1, 5, figsize=[18,8], sharey=True)
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

    # fig, (axs, axs2, axs3, axs4, axs5) = plt.subplots(1, 5, figsize=[9,6])
    # axs.set_title(title)
    # axs.set_xlim(0, len(arr))
    # axs2.set_title(title+"test")
    # axs2.set_xlim(0, len(arr))
    # bars = axs.bar(range(len(arr)), arr, align="edge")
    # bars2 = axs2.bar(range(len(arr)), arr2, align="edge")


    # fig, (bsAxes, ssAxes, isAxes, msAxes, qsAxes) = plt.subplots(1, 5, sharex=True, sharey=True, figsize=[16,6])

    # bsAxes.set_title('Bubble Sort')
    # bsAxes.set_xlim(0, len(arr))
    # bsBar = bsAxes.bar(range(len(arr)), arr, align="edge")

    # ssAxes.set_title('Selection Sort')
    # ssAxes.set_xlim(0, len(arr))
    # ssBar = ssAxes.bar(range(len(arr)), arr2, align="edge")

    # isAxes.set_title('Insertion Sort')
    # isAxes.set_xlim(0, len(arr))
    # isBar = isAxes.bar(range(len(arr)), arr3, align="edge")

    # msAxes.set_title('Merge Sort')
    # msAxes.set_xlim(0, len(arr))
    # msBar = msAxes.bar(range(len(arr)), arr4, align="edge")

    # qsAxes.set_title('Quick Sort')
    # qsAxes.set_xlim(0, len(arr))
    # qsBar = qsAxes.bar(range(len(arr)), arr5, align="edge")

    # visualization = animation.FuncAnimation(fig, func=update_func, fargs=(bars), frames=generator, interval=1, repeat=False)    
    # visualization = selectionSort.getAnimation(fig, arr.copy(), axs) 

    # bs_visualization = animation.FuncAnimation(fig, func=update_fig,
    #     fargs=(bsBar, [0]), frames=bubbleSortGenerator, interval=1,
    #     repeat=False)

    # ss_visualization = animation.FuncAnimation(fig, func=update_fig,
    #     fargs=(ssBar, [0]), frames=selectionSortGenerator, interval=1,
    #     repeat=False)

    # is_visualization = animation.FuncAnimation(fig, func=update_fig,
    #     fargs=(isBar, [0]), frames=insertionSortGenerator, interval=1,
    #     repeat=False)

    # ms_visualization = animation.FuncAnimation(fig, func=update_fig,
    #     fargs=(msBar, [0]), frames=mergeSortGenerator, interval=1,
    #     repeat=False)

    # qs_visualization = animation.FuncAnimation(fig, func=update_fig,
    #     fargs=(qsBar, [0]), frames=quickSortGenerator, interval=1,
    #     repeat=False)

    # plt.show()


# Previous implementation

# def insertionsort(arr):
#     n = len(arr)

#     for nextPos in range(1, n):
#         yield from insert(arr, nextPos)

# def insert(arr, nextPos):
#     nextValue = arr[nextPos]

#     while nextPos > 0 and nextValue < arr[nextPos - 1]:
#         arr[nextPos] = arr[nextPos - 1]
#         nextPos = nextPos - 1
#         yield arr
#     arr[nextPos] = nextValue
    

# def bubblesort(arr):
#     n = len(arr)

#     done = True


#     while done:
#         done = False
#         for i in range(0, n - 1):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 done = True
#                 yield arr
#     return arr
    
# def selectionsort(arr):
#     n = len(arr)

#     posMin = 0

#     for fill in range(0, n):
#         posMin = fill
#         for next in range(fill + 1, n):
#             if (arr[next] < arr[posMin]):
#                 posMin = next
#         arr[fill], arr[posMin] = arr[posMin], arr[fill]
#         yield arr

# def quicksort(arr, left, right):
#     i = left
#     j = right
#     floor = math.floor(left + ((right - left + 1) // 2) - 1)
#     pivot = arr[floor]

#     if (left >= right):
#         return

#     while i <= j:
#         while arr[i] < pivot:
#             i += 1
#         while arr[j] > pivot:
#             j -= 1
#         if i <= j:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             i += 1
#             j -= 1
#             yield arr

#     if left < j:
#         yield from quicksort(arr, left, j)
#     if i < right:
#         yield from quicksort(arr, i, right)

# def mergesort(arr, start, end):
#     if end <= start:
#         return

#     mid = start + ((end - start + 1) // 2) - 1

#     yield from mergesort(arr, start, mid)

#     yield from mergesort(arr, mid + 1, end)

#     yield from merge(arr, start, mid, end)

#     yield arr

# def merge(arr, start, mid, end):

#     array_after_merge = []

#     left = start

#     right = mid + 1

#     while left <= mid and right <= end:

#         if arr[left] < arr[right]:

#             array_after_merge.append(arr[left])

#             left += 1

#         else:
#             array_after_merge.append(arr[right])

#             right += 1

#     while left <= mid:

#         array_after_merge.append(arr[left])

#         left += 1

#     while right <= end:

#         array_after_merge.append(arr[right])

#         right += 1

#     for i, val in enumerate(array_after_merge):

#         arr[start + i] = val

#         yield arr