# 2DD

**2D Dynamic Programming** involves solving problems where the state of each subproblem depends on two parameters, typically represented as `dp[i][j]`. This approach is common in problems where we're working with two dimensions, such as matrices or sequences, and need to optimize over a grid, find patterns across two sequences, or work with two ranges.

### Common 2D Dynamic Programming Problems

1. **Longest Common Subsequence (LCS)**
2. **Edit Distance**
3. **Knapsack Variants**
4. **Matrix Path Problems** (e.g., Minimum Path Sum)
5. **Palindrome Partitioning**

Let's explore some of these problems with examples and code to understand the application of 2D dynamic programming.

---

### 1. Longest Common Subsequence (LCS)

**Problem**: Given two sequences, find the length of the longest subsequence present in both of them.

**Example**:
```
Input: "ABCBDAB", "BDCAB"
Output: 4 (The LCS is "BCAB")
```

**Approach**:
- Use a 2D DP table `dp[i][j]` where `dp[i][j]` represents the LCS length of the substrings `A[0:i]` and `B[0:j]`.
- If `A[i-1] == B[j-1]`, then `dp[i][j] = dp[i-1][j-1] + 1`.
- Otherwise, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

**Code**:

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

**Time Complexity**: O(m * n), where `m` and `n` are the lengths of the two strings.

---

### 2. Edit Distance (Levenshtein Distance)

**Problem**: Find the minimum number of operations required to convert one string into another. Operations are insertion, deletion, and substitution.

**Example**:
```
Input: "sunday", "saturday"
Output: 3 (Operations: insert "a", insert "t", replace "n" with "r")
```

**Approach**:
- Define `dp[i][j]` as the minimum edit distance to convert the first `i` characters of `A` to the first `j` characters of `B`.
- If `A[i-1] == B[j-1]`, `dp[i][j] = dp[i-1][j-1]`.
- If `A[i-1] != B[j-1]`, `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`, corresponding to insert, delete, or substitute.

**Code**:

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

**Time Complexity**: O(m * n)

---

### 3. 0/1 Knapsack Problem

**Problem**: Given a set of items with weights and values, and a knapsack with weight capacity `W`, maximize the value in the knapsack without exceeding `W`. Each item can only be included once.

**Example**:
```
Input: weights = [1, 2, 3], values = [10, 15, 40], W = 5
Output: 55 (Items with weight 2 and 3 are included)
```

**Approach**:
- Define `dp[i][j]` where `dp[i][j]` is the maximum value achievable with the first `i` items and weight limit `j`.
- If `weights[i-1] <= j`, `dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j - weights[i-1]])`.
- Otherwise, `dp[i][j] = dp[i-1][j]`.

**Code**:

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
print(knapsack([1, 2, 3], [10, 15, 40], 5))  # Output: 55
```

**Time Complexity**: O(n * W)

---

### 4. Minimum Path Sum in a Grid

**Problem**: Given a grid of non-negative integers, find a path from the top-left to the bottom-right corner that minimizes the sum of the numbers along the path. You can only move right or down.

**Example**:
```
Input:
[
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
Output: 7 (Path: 1 → 3 → 1 → 1 → 1)
```

**Approach**:
- Define `dp[i][j]` as the minimum path sum to reach cell `(i, j)`.
- For each cell `(i, j)`, `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`.

**Code**:

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

**Time Complexity**: O(m * n)

---

### 5. Palindrome Partitioning (Minimum Cuts)

**Problem**: Given a string `s`, partition it such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning.

**Example**:
```
Input: "aab"
Output: 1 (The palindrome partitioning is ["aa", "b"])
```

**Approach**:
- Use a 2D table `dp[i][j]` where `dp[i][j]` is `True` if `s[i:j+1]` is a palindrome.
- Use another array `cuts[i]` where `cuts[i]` represents the minimum cuts needed for `s[0:i+1]`.

**Code**:

```python
def min_cut(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    cuts = [float('inf')] * n

    for i in range(n):
        for j in range(i + 1):
            if s[j] == s[i] and (i - j < 2 or dp[j + 1][i - 1]):
                dp[j][i] = True

    for i in range(n):
        if dp[0][i]:
            cuts[i] = 0
        else:
            for j in range(i):
                if dp[j + 

1][i]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)

    return cuts[-1]

# Example usage
print(min_cut("aab"))  # Output: 1
```

**Time Complexity**: O(n^2) for both palindrome checking and calculating minimum cuts.

---

### Summary of 2D DP Problems

| **Problem**                 | **Approach**        | **Time Complexity** |
|-----------------------------|---------------------|----------------------|
| Longest Common Subsequence  | Tabulation          | O(m * n)            |
| Edit Distance               | Tabulation          | O(m * n)            |
| 0/1 Knapsack                | Tabulation          | O(n * W)            |
| Minimum Path Sum in Grid    | Tabulation          | O(m * n)            |
| Palindrome Partitioning     | Tabulation & Cuts   | O(n^2)              |

2D Dynamic Programming is effective for problems involving two sequences, grids, or ranges, where each state depends on two indices or parameters. This approach significantly reduces the complexity of problems that would otherwise require exponential time through recursive solutions.