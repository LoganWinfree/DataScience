import numpy as np
import math as m

class step_sort:

    swap_arr = []

    def __init__(self):
        self

    def step(self, arr):
        if len(self.swap_arr) != 0:
            swap = self.swap_arr[0]
            self.swap_arr.pop(0)
            temp = arr[swap[0]]
            arr[swap[0]] = arr[swap[1]]
            arr[swap[1]] = temp
        return arr

    def check(self, arr):
        for x in range(len(arr)-1):
            if arr[x] > arr[x+1]:
                return False
        return True

    def bubble(self, orig_arr):
        arr = orig_arr.copy()
        while self.check(arr) == False:
            for x in range(len(arr)-1):
                if arr[x] > arr[x+1]:
                    self.swap_arr.append((x,x+1))
                    temp = arr[x]
                    arr[x] = arr[x+1]
                    arr[x+1] = temp
    
    def insertion(self, orig_arr):
        arr= orig_arr.copy()
        for x in range(len(arr)):
            i = x
            while i > 0 and arr[i] < arr[i-1]:
                self.swap_arr.append((i,i-1))
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
                i = i - 1
    
    def selection(self, orig_arr):
        arr = orig_arr.copy()
        for x in range(len(arr)):
            i = x
            curr_min = np.inf
            curr_ind = i
            for y in range(i, len(arr)):
                if arr[y] < curr_min:
                    curr_ind = y
                    curr_min = arr[y]
            self.swap_arr.append((x, curr_ind))
            temp = arr[curr_ind]
            arr[curr_ind] = arr[x]
            arr[x] = temp
            

