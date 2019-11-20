import matplotlib.pyplot as plt
import matplotlib.animation as animation

class InsertionSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "InsertionSort"
        # print("Init InsertionSort")

    def sort(self, arr):
        n = len(arr)
        self.spaceUsed = n

        for nextPos in range(1, n):
            self.insert(arr, nextPos)

        return arr

    def insert(self, arr, nextPos):
        nextValue = arr[nextPos]
        self.spaceUsed += 1

        while nextPos > 0 and nextValue < arr[nextPos - 1]:
            arr[nextPos] = arr[nextPos - 1]
            nextPos = nextPos - 1

        arr[nextPos] = nextValue

    def visualSort(self, arr):
        n = len(arr)

        for nextPos in range(1, n):
            yield from self.visualInsert(arr, nextPos)
        yield arr, None, None

    def visualInsert(self, arr, nextPos):
        nextValue = arr[nextPos]

        while nextPos > 0 and nextValue < arr[nextPos - 1]:
            arr[nextPos] = arr[nextPos - 1]
            nextPos = nextPos - 1
            yield arr, nextPos, nextValue
        arr[nextPos] = nextValue
        yield arr, nextPos, nextValue

    def getAnimation(self, arr, fig, axs):

        axs.set_title('Insertion Sort')
        axs.set_xlim(0, len(arr))

        bars = axs.bar(range(len(arr)), arr, align="edge")

        iColor = bars[0].get_facecolor()

        def update_fig(yieldVal):
            arr = yieldVal[0]
            nextPos = yieldVal[1]
            nextValue = yieldVal[2]

            if nextPos == None:  #at the end, set them all back to initial color
                for ind in range(len(arr)):
                    bars[ind].set_facecolor(iColor)
            else:
                for ind in range(len(arr)):
                    if ind == nextPos:
                        bars[ind].set_facecolor([0,0,0])
                        bars[ind].set_height(nextValue)
                    else:
                        bars[ind].set_facecolor(iColor)
                        bars[ind].set_height(arr[ind])

        visualization = animation.FuncAnimation(fig, func=update_fig, frames=self.visualSort(arr), interval=1, repeat=False) 

        return visualization
