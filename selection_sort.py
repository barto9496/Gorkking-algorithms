"""
Selection Sort Algorithm: This algorithm sorts through the whole algorithm and then sorts / sets the smallest element
in the firs place and repeats the process until all the elements are sorted.

The time complexity of the algorithm is really bad as it O(n^2) which isn't a time complexity.
"""


def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_ind = i

        for j in range(i+1, size):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


arr = [-22,71,36,45,-199,-7,12,99]
print(arr)
selection_sort(arr)
print(arr)