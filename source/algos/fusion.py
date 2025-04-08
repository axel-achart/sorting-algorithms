#  Diviser pour régner

"""def fusion_sort(lst):
    sorted_lst = lst.copy()  # No edit original list
    n = len(sorted_lst)

    list1 = sorted_lst[:n // 2]  # First half of the list
    list2 = sorted_lst[n // 2:]  # Second half of the list

    # Sort the two halves recursively
    if len(list1) > 1:
        list1 = fusion_sort(list1)
    if len(list2) > 1:
        list2 = fusion_sort(list2)

    # Merge the sorted halves
    i = j = k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_lst[k] = list1[i]
            i += 1
        else:
            sorted_lst[k] = list2[j]
            j += 1
        k += 1

    # Return the merged sorted list (one)
    sorted_lst = sorted_lst[:k] + list1[i:] + list2[j:]
    return sorted_lst"""

def fusion_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = fusion_sort(lst[:mid])
    right = fusion_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Fusion lists sorted
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    sorted_lst = result.copy()
    # No edit original list

    return sorted_lst