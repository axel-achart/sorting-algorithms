# source/algos/comb_sort.py

def comb_sort(lst):
    sorted_lst = lst.copy()  # Don't modify the original list
    n = len(sorted_lst)
    gap = n
    shrink = 1.3  # The shrink factor for the gap
    swapped = True

    while gap > 1 or swapped:
        # Update the gap for the next comb
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1  # Minimum gap must be 1

        swapped = False

        # Compare and swap elements at the current gap
        for i in range(n - gap):
            if sorted_lst[i] > sorted_lst[i + gap]:
                sorted_lst[i], sorted_lst[i + gap] = sorted_lst[i + gap], sorted_lst[i]
                swapped = True  # Continue sorting if a swap occurred

    return sorted_lst
