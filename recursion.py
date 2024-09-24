def factorial(val):
    if val == 1:
        return 1
    else:
        val = val * factorial(val - 1)
    return val


def arr_sum_calc(arr):
    arr_sum = 0
    sz = len(arr)
    if sz == 0:
        return 0
    if sz == 1:
        return arr[0]
    else:
        arr_sum = arr[0] + arr_sum_calc(arr[1:])
    return arr_sum


def list_sz_calc(arr_sz):
    count = 0
    # print(arr_sz)
    if arr_sz is None:
        return count
    else:
        return 1 + list_sz_calc(arr_sz[1:])


def count_elements(arr):
    # Base case: if the list is empty, return 0
    if not arr:
        return 0
    # Recursive case: add 1 for the first element and call the function on the rest of the list
    return 1 + count_elements(arr[1:])


def max_numb(arr):
    if not arr:
        return 0
    else:
        max_num = max_numb(arr[1:])
        return arr[0] if arr[0] > max_num else max_num


# def binary_search_recursive(arr, guess):
# if not arr:
#     return None
# mid_ind = len(arr) // 2
# if guess == arr[mid_ind]:
#     return mid_ind
# elif guess > arr[mid_ind]:
#     result = binary_search_recursive(arr[mid_ind + 1:], guess)
#     if result is not None:
#         return mid_ind + 1 + result  # Adjusting the index because we sliced the array
#     return None
# else:
#     # val = len(mid_ind-1) + 1
#     return binary_search_recursive(arr[0:mid_ind], guess)

def binary_search_recursive(arr, guess, low=0, high=None):
    if high is None:
        high = len(arr) - 1  # Initialize high for the first call

    # Base case: If the range is invalid, the guess is not found
    if low > high:
        return None

    mid_ind = (low + high) // 2  # Calculate the middle index

    # Check if the guess matches the middle element
    if guess == arr[mid_ind]:
        return mid_ind  # Element found, return the index
    elif guess > arr[mid_ind]:
        # Search in the right half
        return binary_search_recursive(arr, guess, mid_ind + 1, high)
    else:
        # Search in the left half
        return binary_search_recursive(arr, guess, low, mid_ind - 1)


# Example usage:
# sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# guess = 6
# index = binary_search_recursive(sorted_list, guess)
#
# if index is not None:
#     print(f"Element {guess} found at index: {index}")
# else:
#     print(f"Element {guess} not found.")
# Example usage
# my_list = [1, 2, 3, 4, 27, 51]
# print("Length of the list:", binary_search_recursive(my_list, 27))
#
# print("final value: ", list_sz_calc([1, 2, 3, 4]))
#
# print(factorial(5))
#

def binsearch_rec(arr, guess, low = 0 , high=None ):

    if not arr:
        return None
    if high is None:
        high = len(arr) - 1

    mid = (low+high) // 2

    if guess == arr[mid]:
        return mid + 1
    elif guess > mid:
        return binsearch_rec(arr, guess, mid+1, high)
    else:
        return binsearch_rec(arr, guess, low, mid - 1)


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
guess = 6
index = binsearch_rec(sorted_list, guess)
print(index)