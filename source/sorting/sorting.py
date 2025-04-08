# source/sorting/sorting.py

from source.algos.selection_sort import selection_sort
from source.algos.bubble_sort import bubble_sort
from source.algos.comb_sort import comb_sort

# Dictionnaire des algorithmes disponibles
sorting_algorithms = {
    "selection": selection_sort,
    "bubble": bubble_sort,
    "comb": comb_sort,
}
