def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def reverseBubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

def main():
    # Test bubble sort
    a = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(a)
    print ("Sorted array is:", a)

    # Test reverse bubble sort
    a2 = [7, 3243, 23432, 333, 11, 4]
    reverseBubbleSort(a2)
    print ("Reverse sorted array is:", a2)

    # Test quick sort
    a3 = [45, 22, 1, 57, 33, 31, 1]
    quicksort(a3)
    print ("Quick sorted array is:", a3)

# main
main()