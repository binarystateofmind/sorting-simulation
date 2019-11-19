import matplotlib.pyplot as plt
import matplotlib.animation as animation

class BubbleSort:

    def __init__(self):
        self.spaceUsed = 0
        self.name = "BubbleSort"
        print("Init BubbleSort")

    def sort(self, arr):
        n = len(arr)
        self.spaceUsed = n

        done = True
        self.spaceUsed += 1

        while done:
            done = False
            for i in range(0, n - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    done = True
        return arr

    def visualSort(self, arr):
        n = len(arr)

        done = True

        yield arr, 0
        while done:
            done = False
            yield arr, 0
            for i in range(0, n - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    done = True
                yield arr, i+1
        yield arr, -1
        return arr

    def visualizeSorting(self, arr):
        fig, axs = plt.subplots(figsize=[9,6])

        axs.set_title('Bubble Sort')
        axs.set_xlim(0, len(arr))

        bar = axs.bar(range(len(arr)), arr, align="edge")

        def update_fig(arr):
            for ind in range(len(arr)):
                bar[ind].set_height(arr[ind])

        visualization = animation.FuncAnimation(fig, func=update_fig, frames=self.visualSort(arr), interval=1, repeat=False) 

        plt.show()

    def getAnimation(self, arr, fig, axs):

        axs.set_title('Bubble Sort')
        axs.set_xlim(0, len(arr))

        bars = axs.bar(range(len(arr)), arr, align="edge")

        iColor = bars[0].get_facecolor()

        def update_fig(yieldVal):
            arr = yieldVal[0]
            i = yieldVal[1]

            if i == -1:  #at the end, set them all back to initial color
                for ind in range(len(arr)):
                    bars[ind].set_facecolor(iColor)
            else:
                for ind in range(len(arr)):
                    if ind == i:
                        bars[ind].set_facecolor([0,0,0])
                    else:
                        bars[ind].set_facecolor(iColor)
                    bars[ind].set_height(arr[ind])

        visualization = animation.FuncAnimation(fig, func=update_fig, frames=self.visualSort(arr), interval=1, repeat=False) 

        return visualization