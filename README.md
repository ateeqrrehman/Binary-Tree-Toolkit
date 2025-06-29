# Binary-Tree-Toolkit Project

This project was done as part of Data Structure and Algorithm  
The main focus is on working with binary trees, understanding in-order traversal methods (both recursive and iterative), comparing their performance, and checking if a binary tree follows Binary Search Tree (BST) rules.

All functions are implemented in Python and tested using CSV files provided with the assignment. The project also includes time and memory profiling with optional plotting.

---

## 🧠 Project Tasks

The following tasks were completed in this project:

### ✅ 1. Binary Tree Construction
- Builds a binary tree using a level-order (BFS) string input.
- Handles invalid inputs like non-integer tokens or a `None` root with more nodes.
- Example:  
  **Input:** `"1,2,3,None,None,4"`  
  **Output Tree:**
```
  1
 / \
2   3
   /
  4
```

### ✅ 2. In-Order Traversal
- Two versions of in-order traversal were implemented:
- **Recursive**: Uses the call stack.
- **Iterative**: Uses a manual stack.
- Both versions return the same output list and touch every node once.

### ✅ 3. Time and Space Performance Study
- Generates three types of trees:
- **Random**: Random permutation of numbers.
- **Complete**: All levels filled except maybe the last.
- **Skewed**: All nodes linked to either left or right only.
- Compares recursive and iterative in-order traversals on each type.
- Uses:
- `time.perf_counter()` for timing.
- `tracemalloc` for memory profiling.
- `matplotlib` to plot results (optional).
- Runs each setup 50 times to get an average.

### ✅ 4. Binary Search Tree (BST) Validation
- Checks whether a tree satisfies the rules of a BST.
- Makes sure values are strictly increasing from left to right in subtrees.
- Recursively checks each node with valid lower and upper bounds.

---

## 🛠 How to Run

### Requirements
- Python 3.x
- Optional:
- `pandas` (for tables)
- `matplotlib` (for plotting)

### Install (Optional virtual environment)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

### Run

```bash
python Binary_Tree.py
```

---

## 📊 Performance Summary

Timing and memory usage are collected for different input sizes:

| N    | Tree     | Method    | Time (sec) | Peak Bytes |
| ---- | -------- | --------- | ---------- | ---------- |
| 10   | complete | recursive | 8.13×10⁻⁶  | 384.6      |
| 10   | skewed   | iterative | 6.83×10⁻⁶  | 162.2      |
| 100  | complete | recursive | 2.90×10⁻⁵  | 1141.9     |
| 1000 | skewed   | iterative | 1.51×10⁻⁴  | 12448      |
| 2000 | skewed   | recursive | 1.02×10⁻³  | 16383      |

📌 The full results are saved in `traversal_timing.png`.

---

## 📁 Project Structure

```
.
├── Binary_Tree.py           # All main functions and testing logic
├── part1.csv                # Input for part1  and part2 tests
├── part4.csv                # Input for part4 BST tests
├── traversal_timing.png     # Saved plot comparing traversal times
└── README.md                # This file
```

---

## 📌 Highlights

* No use of external tree libraries – all logic is written from scratch.
* BFS string input is safely handled.
* Supports both balanced and worst-case trees (like a linked list).
* Recursion depth errors are handled gracefully.
* Easy to reuse and extend for larger projects.

---

## 📦 Example Extensions

* Add unit tests using `unittest` or `pytest`.
* Add more tree shapes (zigzag, random BSTs).
* Save results to `.csv` or render live plots in Jupyter.

---

## 📄 License

This project is for educational use under MSML 606 Data Structure and Algorithm.
You are free to fork, study, or modify it for learning purposes.

---

**Author:** Ateeq Ur Rehman
Binary-Tree Project

---

Let me know if you’d like:
- a `requirements.txt` file,
- sample CSV input files with detailed dataset.
