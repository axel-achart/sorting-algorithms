The Heron Papyri and sorting algorithms.

# Sorting Algorithms Visualizer

This project is a sorting algorithm visualizer developed in Python using `Tkinter`.  
It allows you to compare different sorting methods both in the **terminal** and via an **animated graphical interface**.

---

## Features

- 7 classic sorting algorithms:
  - Bubble Sort
  - Selection Sort
  - Comb Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort
  
- Interface with:
  - Dropdown menu to select the algorithm
  - List size selector (slider)
  - Visual animation of sorting steps
  - Time comparison chart (using matplotlib)
  - Historical log of all runs (`history.json`)

---

## Project structure
sorting-algorithms/ 
├── source/ 
│ ├── algos/ # One file per sorting algorithm 
│ ├── graphical/ # Tkinter interface + history 
│ ├── terminal/ # Terminal mode 
│ ├── sorting/ # Central sorting function 
├──main.py # Launch file 
├── config.py 
├── README.md

##  Installation

```bash
git clone https://github.com/votre-utilisateur/sorting-algorithms.git
cd sorting-algorithms
pip install matplotlib


##  Comparison of Sorting Algorithms

| Algorithm         | Average Complexity | Worst Case      | Type             | Stable| Notes on 50 elements         |
|-------------------|--------------------|------------------|------------------|------|------------------------------|
| Bubble Sort       | O(n²)              | O(n²)            | Swap-based       |  Yes | Very slow, easy to implement |
| Selection Sort    | O(n²)              | O(n²)            | Selection-based  |  No  | Few swaps, still slow        |
| Comb Sort         | O(n log n) to O(n²)| O(n²)            | Swap (with gap)  |  No  | Faster than bubble sort      |
| Insertion Sort    | O(n²)              | O(n²)            | Insertion-based  |  Yes | Fast on small/near-sorted lists |
| Merge Sort        | O(n log n)         | O(n log n)       | Divide & Conquer |  Yes | Very fast and stable         |
| Quick Sort        | O(n log n)         | O(n²)            | Divide & Conquer |  No  | Fastest in practice, not stable |
| Heap Sort         | O(n log n)         | O(n log n)       | Heap-based       |  No  | Efficient, not stable        |

---

### Notes:

- Quadratic sorts (bubble, insertion, selection) are good for learning, but inefficient on large lists.
- **Merge Sort** is fast and stable but uses more memory.
- **Quick Sort** is usually the fastest in real scenarios, despite its O(n²) worst case.
- **Heap Sort** is reliable and performs well, often used in system-level implementations.
- **Comb Sort** is a simple and effective upgrade over bubble sort for mid-sized lists.

---

For each algorithm, you can:
- Visually observe the sorting behavior
- Compare the **execution times** through live measurement
- View the full sorting history in `history.json`

