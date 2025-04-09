
import time

def heapsort_sort(arr, draw_callback=None, delay=0.01):
    n = len(arr)

    # max heap, build the heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, draw_callback, delay)

    # Extract the elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # switch
        if draw_callback:
            draw_callback(arr)
            time.sleep(delay)
        heapify(arr, i, 0, draw_callback, delay)

    return arr

def heapify(arr, heap_size, root_index, draw_callback=None, delay=0.01):
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        if draw_callback:
            draw_callback(arr)
            time.sleep(delay)
        heapify(arr, heap_size, largest, draw_callback, delay)
