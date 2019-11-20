from tkinter import Tk, Button, Label, Spinbox, Scrollbar
from tkinter import ttk

import bubblesort
import insertionsort
import selectionsort
import quicksort
import mergesort

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import numpy as np


class SortGUI:

    def __init__(self, master):

        self.master = master
        
        master.title("Sorting Algorithms")

        w = 500
        h = 150
        x = 500
        y = 100
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.label_sorts = Label(master, text="Choose a Sorting algorithm:")
        
        self.label_sorts.grid(row=0, column=0)
        
        self.combobox_sorts = ttk.Combobox(master)

        self.combobox_sorts['values'] = ("Quicksort", "Mergesort", "Bubblesort", "Insertionsort", "Selectionsort")
        
        self.combobox_sorts.current(2)
        
        self.combobox_sorts.grid(column=1, row=0)

        self.label_array_type = Label(master, text="Choose array type:")
        
        self.label_array_type.grid(row=1, column=0)
        
        self.combobox_array_type = ttk.Combobox(master)

        self.combobox_array_type['values'] = ("asc", "desc", "log")

        self.combobox_array_type.current(2)

        self.combobox_array_type.bind()
        
        self.combobox_array_type.grid(column=1, row=1, padx=5, pady=5)        

        self.label_size = Label(master, text="Enter size:")
        
        self.label_size.grid(column=0, row=2)

        self.spin_size = Spinbox(master, from_=30, to=300)

        self.spin_size.grid(column=1, row=2)

        self.sort_button = ttk.Button(master, text="Sort", command=self.sort)

        self.sort_button.grid(column=2, row=1)

        self.close_button = ttk.Button(master, text="Close", command=quit)

        self.close_button.grid(column=2, row=2)   

        self.arr = np.random.lognormal(3., 1., int(self.spin_size.get()))

    def arrayType(self):
      
        if self.combobox_array_type.get() == "asc":
            self.arr.sort()

        elif self.combobox_array_type.get() == "desc":
            self.arr = self.arr[::-1]

        elif self.combobox_array_type.get() == "log":
            self.arr =  np.random.lognormal(3., 1., int(self.spin_size.get()))

    def sort(self):

        self.arrayType()

        fig = Figure(figsize=(3,3), dpi=100),

        fig, ax = plt.subplots()

        if self.combobox_sorts.get() == "Selectionsort":

            selectionSort = selectionsort.SelectionSort()

            visualization = selectionSort.getAnimation(self.arr.copy(), fig, ax) 

            plt.show()    

        elif self.combobox_sorts.get() == "Insertionsort":

            insertionSort = insertionsort.InsertionSort()

            visualization = insertionSort.getAnimation(self.arr.copy(), fig, ax) 
            
            plt.show()          

        elif self.combobox_sorts.get() == "Quicksort":
       
            quickSort = quicksort.QuickSort()

            visualization = quickSort.getAnimation(self.arr.copy(), fig, ax) 
            
            plt.show()            

        elif self.combobox_sorts.get() == "Mergesort":
        
            mergeSort = mergesort.MergeSort()

            visualization = mergeSort.getAnimation(self.arr.copy(), fig, ax) 
            
            plt.show()      

        elif self.combobox_sorts.get() == "Bubblesort":
      
            bubbleSort = bubblesort.BubbleSort()
     
            visualization = bubbleSort.getAnimation(self.arr.copy(), fig, ax) 
            
            plt.show()
        

root = Tk()
my_gui = SortGUI(root)
root.mainloop()
def quit():
    global root
    root.quit()
    plt.close('all')