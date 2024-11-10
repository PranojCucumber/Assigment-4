# a method to maintain heap property
def heapify(arr, n, i):
    largest = i  # root of the heap
    left = 2 * i + 1  # index of left child
    right = 2 * i + 2  # index of right child

    # checking if the left and right children are larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

# a method to build max-heap and extraxts elements one by one to sort
def sort_heap(arr):

    n = len(arr)

    # creating the max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extraction of elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swapping of elements
        heapify(arr, i, 0)  # reducing the heap

# output test
arr = [10, 15, 11, 5, 4, 9, 1]
sort_heap(arr)
print("Sorted array:", arr)
