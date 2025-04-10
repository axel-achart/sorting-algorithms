
def selection_sort(lst):
    sorted_lst = lst.copy()
    n = len(sorted_lst)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_lst[j] < sorted_lst[min_index]:
                min_index = j
        sorted_lst[i], sorted_lst[min_index] = sorted_lst[min_index], sorted_lst[i]
    
    return sorted_lst
