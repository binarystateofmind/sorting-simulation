import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class QuickSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "QuickSort"
        # print("Init QuickSort")

    def sort(self, arr):
        self.spaceUsed = len(arr)
        self.quicksort(arr, 0, len(arr) - 1)

    def quicksort(self, arr, left, right):
        i = left
        j = right
        floor = math.floor((left + right) / 2)
        pivot = arr[floor]
        temp = ''
        self.spaceUsed += 6

        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
                j -= 1

        if left < j:
            self.quicksort(arr, left, j)
        if i < right:
            self.quicksort(arr, i, right)

    def visualQuicksort(self, arr, left, right):
        i = left
        j = right
        floor = math.floor(left + ((right - left + 1) // 2) - 1)
        yield arr, left, floor, right, -1, -1
        pivot = arr[floor]

        if (left >= right):
            return

        while i <= j:
            while arr[i] < pivot:
                i += 1
                yield arr, left, pivot, right, i, j
            while arr[j] > pivot:
                j -= 1
                yield arr, left, pivot, right, i, j
            if i <= j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
                j -= 1
            yield arr, left, pivot, right, i, j

        if left < j:
            yield from self.visualQuicksort(arr, left, j)
        if i < right:
            yield from self.visualQuicksort(arr, i, right)
        yield arr, -1, -1, -1, -1, -1

    def getAnimation(self, arr, fig, axs):

        axs.set_title('Quick Sort')
        axs.set_xlim(0, len(arr))

        bars = axs.bar(range(len(arr)), arr, align="edge")

        iColor = bars[0].get_facecolor()

        def update_fig(yieldVal):
            arr = yieldVal[0]
            left = yieldVal[1]
            pivot = yieldVal[2]
            right = yieldVal[3]
            i = yieldVal[4]
            j = yieldVal[5]

            for ind in range(len(arr)):
                if ind == i:
                    bars[ind].set_facecolor([1,0,0])
                elif ind == j:
                    bars[ind].set_facecolor([1,0,0])
                elif ind == pivot:
                    bars[ind].set_facecolor([0,1,0])
                elif ind == left:
                    bars[ind].set_facecolor([0,0,0])
                elif ind == right:
                    bars[ind].set_facecolor([0,0,0])
                else:
                    bars[ind].set_facecolor(iColor)
                bars[ind].set_height(arr[ind])

        visualization = animation.FuncAnimation(fig, func=update_fig, frames=self.visualQuicksort(arr, 0, len(arr) - 1), interval=1, repeat=False) 

        return visualization
