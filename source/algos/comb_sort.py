# source/algos/comb_sort.py

def comb_sort(lst):
    """
    Sorts a list using the Comb Sort algorithm.
    Comb Sort improves on Bubble Sort by using a larger gap between elements
    to eliminate small values (turtles) near the end of the list faster.
    
    Parameters:
        lst (list): The list of numbers to sort.

    Returns:
        list: A new sorted list.
    """
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
