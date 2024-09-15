def binary_search(array_list, item):
    low = 0
    high = len(array_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(my_list, 10))
print(binary_search(my_list, -1))
print(binary_search(my_list, 3))
