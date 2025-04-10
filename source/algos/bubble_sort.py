
def bubble_sort(lst):
    sorted_lst = lst.copy()  
    n = len(sorted_lst)

    for i in range(n):

        swapped = False
        for j in range(0, n - i - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:

                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                swapped = True
        if not swapped:
            break
    
    return sorted_lst