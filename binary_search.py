def binary_search(arr, guess):
    arr_size = len(arr)
    low_index = 0
    high_index = arr_size - 1
    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2

        if guess < arr[mid_index]:
            low_index = mid_index + 1
        if guess > arr[mid_index]:
            high_index = mid_index - 1
        elif guess == arr[mid_index]:
            return mid_index + 1
    return None


print(binary_search([1,2,4,5,61,112,25], 5))
