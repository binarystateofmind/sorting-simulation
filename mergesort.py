import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class MergeSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "MergeSort"
        # print("Init MergeSort")

    def sort(self, arr):
        self.spaceUsed = len(arr)
        self.mergesort(arr)

    def mergesort(self, arr):
        n = len(arr)

        half = n / 2
        self.spaceUsed += 1

        if n > 1:
            left = arr[:math.floor(half)]
            right = arr[math.floor(half):]
            self.spaceUsed += (len(left)+len(right))
            self.mergesort(left)
            self.mergesort(right)
            self.merge(arr, left, right)

        return arr

    def merge(self, arr, left, right):
        i = 0
        j = 0
        k = 0
        self.spaceUsed += 3

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            k = k + 1
            i = i + 1
        while j < len(right):
            arr[k] = right[j]
            k = k + 1
            j = j + 1

        return arr

    def visualMergesort(self, arr, start, end):
        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1

        yield arr, start, end

        yield from self.visualMergesort(arr, start, mid)

        yield from self.visualMergesort(arr, mid + 1, end)

        yield from self.visualMerge(arr, start, mid, end)

        yield arr, -1, -1

    def visualMerge(self, arr, start, mid, end):

        array_after_merge = []

        left = start

        right = mid + 1

        yield arr, left, right

        while left <= mid and right <= end:

            if arr[left] < arr[right]:

                array_after_merge.append(arr[left])

                left += 1

            else:
                array_after_merge.append(arr[right])

                right += 1
        yield arr, left, right

        while left <= mid:

            array_after_merge.append(arr[left])

            left += 1
        yield arr, left, right

        while right <= end:

            array_after_merge.append(arr[right])

            right += 1
        yield arr, left, right

        for i, val in enumerate(array_after_merge):

            arr[start + i] = val

            yield arr, left, right

    def getAnimation(self, arr, fig, axs):

        axs.set_title('Merge Sort')
        axs.set_xlim(0, len(arr))

        bars = axs.bar(range(len(arr)), arr, align="edge")

        iColor = bars[0].get_facecolor()

        def update_fig(yieldVal):
            arr = yieldVal[0]
            left = yieldVal[1]
            right = yieldVal[2]

            for ind in range(len(arr)):
                if ind == left:
                    bars[ind].set_facecolor([1,0,0])
                elif ind == right:
                    bars[ind].set_facecolor([0,0,0])
                else:
                    bars[ind].set_facecolor(iColor)
                bars[ind].set_height(arr[ind])

        visualization = animation.FuncAnimation(fig, func=update_fig, frames=self.visualMergesort(arr, 0, len(arr) - 1), interval=1, repeat=False) 

        return visualization
