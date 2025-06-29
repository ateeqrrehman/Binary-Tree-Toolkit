# from google.colab import drive
# drive.mount('/content/drive')

import csv
import random
import time
import tracemalloc
from collections import deque
import sys

# It is allowing deep recursion for skewed-tree tests
sys.setrecursionlimit(3000)


# NODE
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#HOMEWORK 3
class HomeWork3:
    #Question 1 - Construct a Binary Tree using the given input
    #Input -> BFS representation of a tree
    #output -> The root node of the tree
    #Sample Input -> "1,2,3,None,None,4"
    #There are no duplicate values in the input
    #Output-> Tree Node with 1 as root node, the tree should be as follows
    #         1
    #        / \
    #       2   3
    #          /
    #         4
    def constructBinaryTree(self, input: str) -> TreeNode:
        """
        Reconstruct a binary tree from a BFS string.
        - Trims whitespace, accepts 'None'/''/’null’ for empty nodes.
        - Rejects illegal (non-integer) tokens.
        - Rejects a None root if extra nodes follow.
        Duplicate numeric values are allowed (needed for BST-negative tests).
        """
        if not input or input.strip() == "":
            return None

        toks = [t.strip() for t in input.split(",")]

        legal_none = {"none", "null", ""}
        # basic token sanity (no floats, no letters, etc.)
        for tok in toks:
            low = tok.lower()
            if low in legal_none:
                continue
            if not tok.lstrip("-").isdigit():
                raise ValueError(f"Illegal token: {tok}")

        # root cannot be None when there are more tokens
        if toks[0].lower() in legal_none and len(toks) > 1:
            raise ValueError("Root cannot be None when additional nodes exist")

        if toks[0].lower() in legal_none:
            return None  # single-token empty tree

        root = TreeNode(int(toks[0]))
        q, ix = deque([root]), 1
        while q and ix < len(toks):
            node = q.popleft()
            for side in ("left", "right"):
                if ix >= len(toks):
                    break
                tok = toks[ix].lower()
                if tok not in legal_none:
                    child = TreeNode(int(toks[ix]))
                    if side == "left":
                        node.left = child
                    else:
                        node.right = child
                    q.append(child)
                ix += 1
        return root

    #Question 2 - part 1 Complete the following function for inorder traversal of the tree generated in question 1 in recursive way
    # return an array of elements in inorder traversal
    # ex output for the above mentioned tree -> [2,1,4,3]

    def inOrderTraversalRecursive(self, head: TreeNode) -> list:
        res = []

        def dfs(n):
            if not n:
                return
            dfs(n.left)
            res.append(n.val)
            dfs(n.right)

        dfs(head)
        return res

    #Question 2 - part 2 Complete the following function for inorder traversal of the tree generated in question 1 above in iterative way
    # return an array of elements in inorder traversal
    # ex output for the above mentioned tree -> [2,1,4,3]
    def inOrderTraversalIterative(self, head: TreeNode) -> list:
        res, stk, cur = [], [], head
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    #Question 3: Time and space complexity analysis 
    
    # (a) Write a function to generate a random permutation of N unique numbers.
    def generate_random_permutation(self, N) -> list:
        return random.sample(range(1, N + 1), N)

    # (b) Write a function to generate a complete binary tree given N unique numbers.
    def generate_complete_tree(self, nums) -> TreeNode:
        if not nums:
            return None
        nodes = [TreeNode(v) for v in nums]
        for i, n in enumerate(nodes):
            l, r = 2 * i + 1, 2 * i + 2
            if l < len(nodes):
                n.left = nodes[l]
            if r < len(nodes):
                n.right = nodes[r]
        return nodes[0]

    # (c) Write a function to generate a skewed binary tree (all left or all right children) given N unique numbers.
    def generate_skewed_tree(self, nums, skew="left")  -> TreeNode:
        if not nums:
            return None
        root = TreeNode(nums[0])
        cur = root
        for v in nums[1:]:
            nxt = TreeNode(v)
            if skew == "left":
                cur.left = nxt
            else:
                cur.right = nxt
            cur = nxt
        return root

    # Helper for timing / memory study
    def compare_traversals(self, sizes=(10, 100, 1000, 2000), iterations=30):
        """
        Return rows: (N, tree_type, method, mean_sec, mean_peak_bytes).
        If recursion depth blows up, NaNs are recorded for that entry.
        """
        rows = []
        for N in sizes:
            nums = self.generate_random_permutation(N)
            for ttype, root in (
                ("complete", self.generate_complete_tree(nums)),
                ("skewed", self.generate_skewed_tree(nums)),
            ):
                for tag, func in (
                    ("recursive", self.inOrderTraversalRecursive),
                    ("iterative", self.inOrderTraversalIterative),
                ):
                    tot_t = tot_m = valid = 0
                    for _ in range(iterations):
                        tracemalloc.start()
                        try:
                            t0 = time.perf_counter()
                            func(root)
                            dur = time.perf_counter() - t0
                            _, peak = tracemalloc.get_traced_memory()
                        except RecursionError:
                            dur = float("nan")
                            peak = float("nan")
                        finally:
                            tracemalloc.stop()
                        if dur == dur:  # skip NaNs
                            tot_t += dur
                            tot_m += peak
                            valid += 1
                    rows.append(
                        (
                            N,
                            ttype,
                            tag,
                            (tot_t / valid) if valid else float("nan"),
                            (tot_m / valid) if valid else float("nan"),
                        )
                    )
        return rows

  # Question 4: Validate Binary Search Tree (BST)
    
    # Write a function to check if a given binary tree satisfies BST properties.
    # Input:
    #   - The root node of the binary tree. This root node should be generated from a level-by-level representation 
    # (i.e., BFS output) of a binary tree. You may use the function you implemented for Problem 1 to construct this tree. 
    # Output:
    #   - Return True if the tree satisfies BST properties; otherwise return False.
    def validateBST(self, head: TreeNode)  -> bool:
        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(
                node.right, node.val, high
            )

        return helper(head, float("-inf"), float("inf"))


#Main Function Do not edit the code below
if __name__ == "__main__":
    homework3 = HomeWork3()

    # QUESTION 1 and 2
    testcasesforquestion1 = []
    try:
        with open("question1.csv", "r") as file:
            testCases = csv.reader(file)
            for row in testCases:
                testcasesforquestion1.append(row)
    except FileNotFoundError:
        print("File Not Found")

    print("RUNNING TEST CASES FOR QUESTIONS 1 and 2 ")
    #Running Test Cases for Question 1 and 2
    for row, (inputValue, expectedOutput) in enumerate(testcasesforquestion1, start=1):
        if (expectedOutput == ""):
             expectedOutput=[]
        else:
            expectedOutput=expectedOutput.split(",")
            for i in range(len(expectedOutput)):
                expectedOutput[i]=int(expectedOutput[i])
        root = homework3.constructBinaryTree(inputValue)
        recursiveOutput = homework3.inOrderTraversalRecursive(root)
        iterativeOutput = homework3.inOrderTraversalIterative(root)
        assert iterativeOutput == recursiveOutput == expectedOutput, f"Test Case {row} Failed: traversal outputs do not match"
        print(f"Test case {row} Passed")

    # QUESTION 4
    testcasesForQuestion4 = []
    try:
        with open("question4.csv", "r") as file:
            testCases = csv.reader(file)
            for row in testCases:
                testcasesForQuestion4.append(row)
    except FileNotFoundError:
        print("question4.csv File Not Found")

    if testcasesForQuestion4:
        print("\nRUNNING TEST CASES FOR QUESTION 4")
        # Each test case: first field is the BFS string, second is expected BST result ("True" or "False")
        for idx, (inputValue, expectedBST) in enumerate(testcasesForQuestion4, start=1):
            expectedBST = True if expectedBST.strip() == "True" else False
            root = homework3.constructBinaryTree(inputValue)
            result = homework3.validateBST(root)
            assert result == expectedBST, f"Test Case {idx} Failed: For input [{inputValue}], expected {expectedBST} but got {result}"
            print(f"Test case {idx} Passed")

    # QUESTION 3 TIMING / MEMORY STUDY
    print("\nGENERATING TIMING / MEMORY TABLE")
    rows = homework3.compare_traversals(
        sizes=(10, 100, 1000, 2000), iterations=50
    )

    try:
        import pandas as pd

        df = pd.DataFrame(
            rows, columns=["N", "tree", "method", "sec", "peak_B"]
        )
        print(df.to_markdown(index=False))
    except ImportError:
        print("pandas not installed; raw rows:")
        for r in rows:
            print(r)

    try:
        import matplotlib.pyplot as plt

        plt.figure()
        for ttype in ("complete", "skewed"):
            for meth, style in (("recursive", "-o"), ("iterative", "-x")):
                sub = [r for r in rows if r[1] == ttype and r[2] == meth]
                if sub:
                    Ns = [r[0] for r in sub]
                    secs = [r[3] for r in sub]
                    plt.plot(Ns, secs, style, label=f"{ttype}-{meth}")
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("N")
        plt.ylabel("seconds (avg of 50 runs)")
        plt.title("In-order traversal timing")
        plt.legend()
        plt.tight_layout()
        plt.savefig("traversal_timing.png")
        print("\nPlot saved as traversal_timing.png")
    except ImportError:
        print("matplotlib not installed; skipping plot")

    print("\nAll tests passed successfully!")

