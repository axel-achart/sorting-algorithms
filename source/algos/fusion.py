#  Diviser pour régner

from config import *
import time


def fusion_sort(lst, draw_callback=None, delay=0):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = fusion_sort(lst[:mid], draw_callback, delay)
    right = fusion_sort(lst[mid:], draw_callback, delay)

    return merge(left, right, draw_callback, delay)

def merge(left, right, draw_callback=None, delay=0):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if draw_callback:
            draw_callback(result + left[i:] + right[j:], color=COLOR_SIX)
            time.sleep(delay)

    result.extend(left[i:])
    result.extend(right[j:])

    if draw_callback:
        draw_callback(result, color=COLOR_SIX)
        time.sleep(delay)

    return result