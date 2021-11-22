import random
import time
import sys
from numpy.random import randint



def randomInput(list_size):
    forSort = []
    i=0
    while i<list_size:
        n=random.randint(-5000,25000)
        forSort.append(n)
        i +=1
    print(*forSort)
    return forSort


def BubbleSort(arr):
    rValues = []
    rValues = arr
    number = len(rValues)
    for x in range(0, number - 1):
        y=0
        while(y < number -1 -x):

            if rValues[y] > rValues[y + 1]:
                temp = rValues[y]
                rValues[y] = rValues[y + 1]
                rValues[y + 1] = temp
            y = y + 1
        x = x + 1
    print("Sorted elements for bubble sort:")
    print(*rValues)


def InsertionSort(arr):
    rValues = []
    rValues = arr
    number = len(rValues)
    for i in range(0, number):
        key = rValues[i]
        j = i - 1
        while j >= 0 and key < rValues[j]:
            rValues[j + 1] = rValues[j]
            j-=1
        rValues[j + 1] = key
    print("Sorted elements for insertion sort:")
    print(*rValues)


def SelectionSort(arr):
    rValues = []
    rValues = arr
    number = len(rValues)
    for i in range(0, number - 1):

        min = i
        x = i
        while(x + 1 < len(arr)):
                x += 1
                j = x
                if arr[min] > arr[j]:
                    min = j
    print("Sorted elements for selection sort :")
    print(*rValues)


def MergeSort(arr):
    rValues = []
    rValues = arr

    def sorting(x, y):
        Mer = []
        i = 0
        j = 0
        while i < len(x) and j < len(y):
            if x[i] < y[j]:
                Mer.append(x[i])
                i += 1
            else:
                Mer.append(y[j])
                j += 1
        if i == len(x):
            Mer.extend(y[j:])
        else:
            Mer.extend(x[i:])
        return Mer

    def merge(rValues):
        if len(rValues) <= 1:
            return rValues
        mid = len(rValues) // 2
        LeftValues = merge(rValues[:mid])
        RightValues = merge(rValues[mid:])
        return sorting(LeftValues, RightValues)

    sorted = []
    sorted = merge(rValues)
    print("Sorted elements for merge sort :")
    print(*sorted)


def HeapSort(arr):
    rValues = []
    rValues = arr
    n = len(rValues)

    def MaxHeap(rValues, n, i):

        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and rValues[i] < rValues[l]:
            max = l
        else:
            max = i

        if r < n and rValues[max] < rValues[r]:
            max = r

        if max != i:
            temp = rValues[max]
            rValues[max] = rValues[i]
            rValues[i] = temp
            MaxHeap(rValues, n, max)

    for i in range(n // 2 - 1, -1, -1):
        MaxHeap(rValues, n, i)

    for i in range(n - 1, 0, -1):
        temp = rValues[i]
        rValues[i] = rValues[0]
        rValues[0] = temp
        MaxHeap(rValues, i, 0)
    print("Sorted elements for heap sort :")
    print(*rValues)


def RegularQuickSort(arr):
    rValues = []
    rValues = arr


    def Quicksort(rValues):
        n = len(rValues)
        if n <= 1:
            return rValues
        else:
            pivot = rValues.pop()
        large = []
        small = []
        for item in rValues:
            if item > pivot:
                large.append(item)
            else:
                small.append(item)
        return Quicksort(small) + [pivot] + Quicksort(large)




    print("Sorted elements for quick sort :")
    print(*rValues)


def SpecialQuickSort(arr):
    rValues = []
    rValues = arr
    n = len(rValues)

    def median3(rValues, begin, end):
        middle = (begin + end) // 2

        if rValues[begin] <= rValues[middle] <= rValues[end]:
            return rValues[middle], middle
        if rValues[begin] <= rValues[end] <= rValues[middle]:
            return rValues[end], end
        if rValues[middle] <= rValues[begin] <= rValues[end]:
            return rValues[begin], begin
        if rValues[end] <= rValues[middle] <= rValues[begin]:
            return rValues[middle], middle
        if rValues[middle] <= rValues[end] <= rValues[begin]:
            return rValues[end], end
        if rValues[end] <= rValues[begin] <= rValues[middle]:
            return rValues[begin], begin

    def QuickSortRecursion(rValues, begin, end):
        if begin < end:
            sp = partition(rValues, begin, end)
            QuickSortRecursion(rValues, begin, sp - 1)
            QuickSortRecursion(rValues, sp + 1, end)

    def partition(rValues, begin, end):
        pivot, index = median3(rValues, begin, end)
        rValues[begin], rValues[index] = rValues[index], rValues[begin]

        i = begin + 1
        j = end
        done = False
        while not done:
            while i <= j and rValues[i] <= pivot:
                i += 1
            while i <= j and rValues[j] >= pivot:
                j -= 1
            if j < i:
                done = True
            else:
                rValues[i], rValues[j] = rValues[j], rValues[i]
        rValues[j], rValues[begin] = rValues[begin], rValues[j]

        return j

    QuickSortRecursion(rValues, 0, n - 1)
    print("Sorted elements for quick sort using 3 medians sort :")
    print(*rValues)


def MainSort():
    print("==================================================================================================================")
    print(" \n \t DSGN & ANLY ALGORITHMS PROJECT BY SUDHARSAN RAJAM \n")
    print("\t \t \t UTA ID: 1001874246 \n")
    list_size = input("Enter the size of list to be sorted \t")
    list_size = int(list_size)
    print("\n")
    rValues = randomInput(list_size)



    print("\n1. MERGE SORT \n")
    print("2. HEAP SORT \n")
    print("3. REGULAR QUICK SORT \n")
    print("4. QUICK SORT USING 3 MEDIANS \n")
    print("5. INSERTION SORT \n")
    print("6. SELECTION SORT \n")
    print("7. BUBBLE SORT \n")
    print("8. COMPARE ALL OF THE ABOVE ALGORITHMS AND THEIR RUNNING TIME \n")
    option = input("CHOOSE FROM 1 - 8 TO PERFORM THE SORTING ALGOS \n")
    option = int(option)
    
    if option == 1:

        input_time = time.time()
        MergeSort(rValues)
        final_time = time.time()
        Total_Merge_Time=final_time-input_time
        print(f"Time taken to sort using Merge sort algo {Total_Merge_Time}")
    
    elif option == 2:

        input_time = time.time()
        HeapSort(rValues)
        final_time = time.time()
        Total_Heap_Time=final_time-input_time
        print(f"Time taken to sort using Heap sort algorithm {Total_Heap_Time}")
       
    elif option == 3:

        input_time = time.time()
        RegularQuickSort(rValues)
        final_time = time.time()
        Total_Quick_Time=final_time-input_time
        print(f"Time taken to sort using Regular Quick sort algorithm {Total_Quick_Time}")
    
    elif option == 4:

        input_time = time.time()
        SpecialQuickSort(rValues)
        final_time = time.time()
        Total_Special_Quick_Time=final_time-input_time
        print(f"Time taken to sort using Quick sort algorithm with 3 median {Total_Special_Quick_Time}")
    
    elif option == 5:

        input_time = time.time()
        InsertionSort(rValues)
        final_time = time.time()
        Total_Insertion_Time=final_time-input_time
        print(f"Time taken to sort using Insertion sort algorithm {Total_Insertion_Time}")
    
    elif option == 6:

        input_time = time.time()
        SelectionSort(rValues)
        final_time = time.time()
        Total_Selection_Time=final_time-input_time
        print(f"Time taken to sort using Selection sort algorithm {Total_Selection_Time}")
    
    elif option == 7:

        input_time = time.time()
        BubbleSort(rValues)
        final_time = time.time()
        Total_Bubble_Time=final_time-input_time
        print(f"Time taken to sort using Bubble sort algorithm {Total_Bubble_Time}")

    elif option == 8:
        input_time = time.time()
        MergeSort(rValues)
        final_time = time.time()
        Total_Merge_Time=final_time-input_time

        input_time = time.time()
        HeapSort(rValues)
        final_time = time.time()
        Total_Heap_Time = final_time - input_time

        input_time = time.time()
        # sys.setrecursionlimit(1000000)
        RegularQuickSort(rValues)
        final_time = time.time()
        Total_Quick_Time = final_time - input_time

        input_time = time.time()
        SpecialQuickSort(rValues)
        final_time = time.time()
        Total_Special_Quick_Time = final_time - input_time

        input_time = time.time()
        InsertionSort(rValues)
        final_time = time.time()
        Total_Insertion_Time = final_time - input_time

        input_time = time.time()
        SelectionSort(rValues)
        final_time = time.time()
        Total_Selection_Time = final_time - input_time

        input_time = time.time()
        BubbleSort(rValues)
        final_time = time.time()
        Total_Bubble_Time = final_time - input_time

        print(f"\nMerge Sort Algorithm Time \t \t {Total_Merge_Time}")
        print(f"Heap Sort Algorithm Time \t \t {Total_Heap_Time}")
        print(f"Quick Sort Algorithm Time \t \t {Total_Quick_Time}")
        print(f"Quick Sort Algorithm with 3 Median Time  {Total_Special_Quick_Time}")
        print(f"Insertion Sort Algorithm Time \t \t {Total_Insertion_Time}")
        print(f"Selection Sort Algorithm Time \t \t {Total_Selection_Time}")
        print(f"Bubble Sort Algorithm Time \t \t {Total_Bubble_Time}")


    else:
        print("PLEASE GIVE A VALID INPUT")

    MainSort()

MainSort()