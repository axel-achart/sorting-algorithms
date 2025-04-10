from config import *
import time

def heapsort_sort(lst, draw_callback=None, delay=0.01):
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i, draw_callback, delay)

    for i in range(n - 1, 0, -1):

        lst[i], lst[0] = lst[0], lst[i]


        if draw_callback:
            draw_callback(lst, color=COLOR_SEVEN)
            time.sleep(delay)


        heapify(lst, i, 0, draw_callback, delay)
    return lst

def heapify(lst, heap_size, root_index, draw_callback=None, delay=0.01):
    largest = root_index 
    left = 2 * root_index + 1  
    right = 2 * root_index + 2

    if left < heap_size and lst[left] > lst[largest]:
        largest = left

    if right < heap_size and lst[right] > lst[largest]:
        largest = right

    if largest != root_index:
        lst[root_index], lst[largest] = lst[largest], lst[root_index]

        if draw_callback:
            draw_callback(lst, color=COLOR_SEVEN)
            time.sleep(delay)

        heapify(lst, heap_size, largest, draw_callback, delay)