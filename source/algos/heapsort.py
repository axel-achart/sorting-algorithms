from config import *
import time

def heapsort_sort(lst, draw_callback=None, delay=0.01):
    n = len(lst)

    # Step 1: Build a max heap from the input list
    # We start from the last non-leaf node and call heapify
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i, draw_callback, delay)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (maximum value) to the end of the array
        lst[i], lst[0] = lst[0], lst[i]

        # Optional: visualize the array after each swap
        if draw_callback:
            draw_callback(lst)
            time.sleep(delay)

        # Call heapify on the reduced heap (ignore the sorted part at the end)
        heapify(lst, i, 0, draw_callback, delay)
    return lst

# Helper function to heapify a subtree rooted at index root_index
def heapify(lst, heap_size, root_index, draw_callback=None, delay=0.01):
    largest = root_index        # Assume root is the largest
    left = 2 * root_index + 1   # Left child index
    right = 2 * root_index + 2  # Right child index

    # If left child exists and is greater than root
    if left < heap_size and lst[left] > lst[largest]:
        largest = left

    # If right child exists and is greater than current largest
    if right < heap_size and lst[right] > lst[largest]:
        largest = right

    # If root is not the largest, swap with the largest child
    if largest != root_index:
        lst[root_index], lst[largest] = lst[largest], lst[root_index]

        # Optional: visualize the array after each swap
        if draw_callback:
            draw_callback(lst, color=COLOR_SEVEN)
            time.sleep(delay)

        # Recursively heapify the affected subtree
        heapify(lst, heap_size, largest, draw_callback, delay)