# source/sorting/sorting.py

from source.algos.selection_sort import selection_sort
from source.algos.bubble_sort import bubble_sort
from source.algos.insertion import insertion_sort
from source.algos.heapsort import heapsort_sort
from source.algos.fusion import fusion_sort
from source.algos.fast import fast_sort
from source.algos.combsort import combsort_sort

# Dictionary algorithm
sorting_algorithms = {
    "selection": selection_sort,
    "bubble": bubble_sort,
    "insertion": insertion_sort,
    "heapsort": heapsort_sort,
    "fusion": fusion_sort,
    "fast": fast_sort,
    "compsort": combsort_sort
}
