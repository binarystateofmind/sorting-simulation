import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SelectionSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "SelectionSort"
        print("Init SelectionSort")

    def sort(self, arr):
        n = len(arr)
        self.spaceUsed = n

        posMin = 0
        self.spaceUsed += 1

        for fill in range(0, n):
            posMin = fill
            for next in range(fill + 1, n):
                if (arr[next] < arr[posMin]):
                    posMin = next
            arr[fill], arr[posMin] = arr[posMin], arr[fill]

        return arr

    def visualSort(self, arr):
        n = len(arr)

        posMin = 0

        for fill in range(0, n):
            posMin = fill
            for next in range(fill + 1, n):
                if (arr[next] < arr[posMin]):
                    posMin = next
                    yield arr, next, posMin
                else:
                    yield arr, next, posMin
            arr[fill], arr[posMin] = arr[posMin], arr[fill]
            yield arr, next, posMin
        yield arr, None, None

    def visualizeSorting(self, arr):
        fig, axs = plt.subplots(figsize=[9,6])

        axs.set_title('Selection Sort')
        axs.set_xlim(0, len(arr))

        bar = axs.bar(range(len(arr)), arr, align="edge")

        def update_fig(arr):
            for ind in range(len(arr)):
                bar[ind].set_height(arr[ind])

        visualization = animation.FuncAnimation(fig, func=update_fig, frames=self.visualSort(arr), interval=1, repeat=False) 

        plt.show()

    def getAnimation(self, arr, fig, axs):

        axs.set_title('Selection Sort')
        axs.set_xlim(0, len(arr))

        bars = axs.bar(range(len(arr)), arr, align="edge")

        iColor = bars[0].get_facecolor()

        def update_fig(yieldVal):
            arr = yieldVal[0]

            if yieldVal[1] == None:  #at the end, set them all back to initial color
                for ind in range(len(arr)):
                    bars[ind].set_facecolor(iColor)
            else:
                n = yieldVal[1]
                minPos = yieldVal[2]

                for ind in range(len(arr)):
                    if ind == minPos:
                        bars[ind].set_facecolor([1,0,0])
                    elif ind == n:
                        bars[ind].set_facecolor([0,0,0])
                    else:
                        bars[ind].set_facecolor(iColor)
                    bars[ind].set_height(arr[ind])

        visualization = animation.FuncAnimation(fig, func=update_fig, frames=self.visualSort(arr), interval=1, repeat=False) 

        return visualization
