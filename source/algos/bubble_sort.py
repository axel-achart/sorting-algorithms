# source/algos/bubble_sort.py

def bubble_sort(lst):
    sorted_lst = lst.copy()  # No edit original list
    n = len(sorted_lst)

    for i in range(n):
        # Verif if list is already sorted or not
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                # Switch elements
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                swapped = True
        if not swapped:
            break
    
    return sorted_lst