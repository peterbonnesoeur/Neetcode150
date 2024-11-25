# 1-DD

**Dynamic Programming (DP)** is a powerful algorithmic technique for solving problems by breaking them down into overlapping subproblems. Each subproblem is solved only once, and its solution is stored (usually in a table or array) to avoid redundant computations. DP is especially effective for problems involving optimization, counting, and partitioning.

### Key Concepts in Dynamic Programming

1. **Optimal Substructure**: A problem exhibits optimal substructure if its optimal solution can be constructed from the optimal solutions of its subproblems.
  
2. **Overlapping Subproblems**: A problem has overlapping subproblems if it can be broken down into subproblems that are solved multiple times. DP is efficient for such problems because it avoids redundant calculations by storing results.

3. **Memoization vs. Tabulation**:
   - **Memoization**: A top-down approach where results of subproblems are stored as they are computed (usually with recursion and a cache).
   - **Tabulation**: A bottom-up approach where solutions to subproblems are built iteratively, filling a table from smaller to larger subproblems.

---

### Common Types of DP Problems

1. **Fibonacci Sequence**
2. **Knapsack Problems**
3. **Longest Common Subsequence (LCS)**
4. **Edit Distance**
5. **Coin Change**
6. **Partition Problem**
7. **Minimum Path Sum**
8. **Matrix Chain Multiplication**

Let’s explore these with explanations, examples, and code.

---

### 1. Fibonacci Sequence

**Problem**: Find the nth Fibonacci number, where `Fib(n) = Fib(n-1) + Fib(n-2)` and `Fib(0) = 0`, `Fib(1) = 1`.

**Recursive DP (Memoization)**:

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Example usage
print(fib_memo(10))  # Output: 55
```

**Iterative DP (Tabulation)**:

```python
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

# Example usage
print(fib_tab(10))  # Output: 55
```

**Time Complexity**: O(n) for both approaches.

---

### 2. Knapsack Problem

**Problem**: Given a list of items with weights and values, and a knapsack with a weight capacity `W`, maximize the value in the knapsack without exceeding `W`. Each item can only be included once (0/1 Knapsack).

**Solution Approach (Tabulation)**:
- Use a DP table where `dp[i][j]` represents the maximum value achievable with the first `i` items and weight limit `j`.

**Code Example**:

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j - weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][W]

# Example usage
weights = [1, 2, 3]
values = [10, 15, 40]
W = 5
print(knapsack(weights, values, W))  # Output: 55
```

**Time Complexity**: O(n * W), where `n` is the number of items and `W` is the knapsack capacity.

---

### 3. Longest Common Subsequence (LCS)

**Problem**: Given two strings, find the length of their longest common subsequence (a sequence of characters that appears in both strings in the same order).

**Solution Approach (Tabulation)**:
- Use a 2D DP table where `dp[i][j]` represents the length of the LCS for substrings of the first `i` characters of string `A` and the first `j` characters of string `B`.

**Code Example**:

```python
def lcs(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Example usage
print(lcs("ABCBDAB", "BDCAB"))  # Output: 4
```

**Time Complexity**: O(m * n), where `m` and `n` are the lengths of the strings.

---

### 4. Edit Distance

**Problem**: Given two strings `A` and `B`, find the minimum number of operations required to convert `A` into `B`. Allowed operations are insertion, deletion, and substitution.

**Solution Approach (Tabulation)**:
- Use a 2D DP table where `dp[i][j]` represents the minimum edit distance between the first `i` characters of `A` and the first `j` characters of `B`.

**Code Example**:

```python
def edit_distance(A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]

# Example usage
print(edit_distance("sunday", "saturday"))  # Output: 3
```

**Time Complexity**: O(m * n).

---

### 5. Coin Change

**Problem**: Given an integer array `coins` representing coin denominations and an integer `amount`, find the minimum number of coins that make up `amount`.

**Solution Approach (Tabulation)**:
- Use a 1D DP array where `dp[i]` represents the minimum number of coins needed for amount `i`.

**Code Example**:

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
print(coin_change([1, 2, 5], 11))  # Output: 3
```

**Time Complexity**: O(n * amount), where `n` is the number of coins.

---

### 6. Minimum Path Sum

**Problem**: Given a grid of non-negative integers, find a path from the top-left to the bottom-right that minimizes the sum of the numbers along the path. You can only move right or down.

**Solution Approach (Tabulation)**:
- Use a 2D DP table where `dp[i][j]` represents the minimum path sum to reach cell `(i, j)`.

**Code Example**:

```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

# Example usage
grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
print(min_path_sum(grid))  # Output: 7
```

**Time Complexity**: O(m * n), where `m` and `n` are the grid dimensions.

---

### Summary of Dynamic Programming

| **Problem**           | **Approach**             | **

Complexity**   | **Explanation**                                  |
|-----------------------|--------------------------|-------------------|--------------------------------------------------|
| Fibonacci Sequence    | Memoization or Tabulation| O(n)             | Avoid redundant calculations for each Fib(n).    |
| Knapsack              | Tabulation               | O(n * W)         | Maximize value without exceeding weight W.       |
| Longest Common Subseq | Tabulation               | O(m * n)         | Finds the longest subsequence present in both.   |
| Edit Distance         | Tabulation               | O(m * n)         | Transform one string to another with minimal ops.|
| Coin Change           | Tabulation               | O(n * amount)    | Find min coins for given amount.                 |
| Minimum Path Sum      | Tabulation               | O(m * n)         | Minimize the sum from top-left to bottom-right.  |

Dynamic Programming is versatile for solving a wide variety of problems, especially those with overlapping subproblems and optimal substructure. Its efficiency often lies in converting exponential recursive problems to polynomial solutions.