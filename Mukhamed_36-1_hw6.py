def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def binary_search(element, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Применяем сортировку (выберите bubble_sort или selection_sort)
unsorted_list = [4, 2, 7, 1, 9, 3]
sorted_list = bubble_sort(unsorted_list.copy())

# Применяем двоичный поиск
element_to_search = 7
result = binary_search(element_to_search, sorted_list)

print("Отсортированный список:", sorted_list)
print(f"Индекс элемента {element_to_search}:", result)






