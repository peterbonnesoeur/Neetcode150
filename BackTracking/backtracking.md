# Backtracking

**Backtracking** is an algorithmic technique used for solving problems incrementally by building potential solutions and abandoning ("backtracking" from) solutions as soon as it becomes clear that they cannot lead to a valid or optimal answer. This approach is often used for **combinatorial problems** where multiple solutions or paths are possible, such as generating permutations, subsets, or solving constraint-based puzzles.

Backtracking is generally implemented using a **recursive approach**, and it tries each possible option at each step, going deeper only if the current option still satisfies the problem constraints. If a constraint is violated, the algorithm backtracks to explore other options.

The logic of backtracking, follows a general pattern that can be summarized into the following steps:

### 1. **Choice**:
At each step, you have a set of choices. These could be which element to add to a permutation, which path to take in a maze, which value to assign to a variable in a puzzle, etc. In the permutation example, the choice is which remaining element to add next to the current permutation.

### 2. **Constraints**:
There are constraints that must be respected. In a permutation, a key constraint is that no element can appear more than once. In other types of problems, constraints could be more complex, like the rules of Sudoku, the safe path in a maze, or the valid subset in a combination problem.

### 3. **Goal**:
There is a clear goal to be reached, which determines when a solution is complete. In permutations, the goal is reached when a permutation includes all the original elements exactly once. In other problems, the goal could be reaching the end of a maze, satisfying all conditions of a puzzle, or finding all possible combinations that meet certain criteria.


### Key Concepts in Backtracking

1. **Decision Tree**: Backtracking often explores solutions by constructing a decision tree. Each node represents a state, and each branch represents a possible choice that leads to a new state.
  
2. **Pruning**: Pruning is an optimization in backtracking where branches of the tree that cannot lead to valid solutions are "pruned" early, reducing the number of recursive calls and improving efficiency.

3. **Base Case and Recursive Case**: The base case is the condition where the solution is complete or invalid, and backtracking stops. The recursive case is where the algorithm explores further by making choices.

### Common Problems Solved by Backtracking

1. **Permutations**
2. **Subsets (Power Set)**
3. **N-Queens Problem**
4. **Sudoku Solver**
5. **Combination Sum**
6. **Rat in a Maze**
7. **Word Search on a Grid**

Let's discuss each problem type with explanations, examples, and code to understand how backtracking is applied.

---

### 1. **Permutations of a List**

**Problem**: Given a list of unique integers, generate all possible permutations.

**Example**:
```
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

**Solution Approach**:
- Use backtracking to build permutations by picking one element at a time.
- Use a temporary list to build each permutation.
- If all elements are used, add the permutation to the result list.

**Code Example**:

```python
def permute(nums):
    def backtrack(path, used, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack(path, used, res)
            path.pop()  # Undo the choice
            used[i] = False  # Mark as unused
    
    result = []
    backtrack([], [False] * len(nums), result)
    return result

# Example usage
print(permute([1, 2, 3]))
```

**Time Complexity**: O(n * n!), where `n` is the number of elements. Generating all permutations involves `n!` permutations, and copying each permutation takes O(n) time.

---

### 2. **Subsets (Power Set)**

**Problem**: Given a set of distinct integers, generate all possible subsets (the power set).

**Example**:
```
Input: [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

**Solution Approach**:
- Use backtracking to include or exclude each element.
- Recursively explore subsets that include the current element, then backtrack to explore subsets that exclude it.

**Code Example**:

```python
def subsets(nums):
    def backtrack(start, path, res):
        res.append(path[:])  # Add current subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, res)
            path.pop()  # Undo the choice
    
    result = []
    backtrack(0, [], result)
    return result

# Example usage
print(subsets([1, 2, 3]))
```

**Time Complexity**: O(2^n), where `n` is the number of elements. Each element has two choices: included or excluded.

---

### 3. **N-Queens Problem**

**Problem**: Place `n` queens on an `n x n` chessboard such that no two queens threaten each other.

**Example**:
```
Input: n = 4
Output: [
  [".Q..", "...Q", "Q...", "..Q."],
  ["..Q.", "Q...", "...Q", ".Q.."]
]
```

**Solution Approach**:
- Use backtracking to place queens row by row.
- Check if the placement is safe (no queens on the same row, column, or diagonal).
- If safe, place a queen and move to the next row. If not, backtrack.

**Code Example**:

```python
def solve_n_queens(n):
    def is_safe(row, col):
        return not cols[col] and not diag1[row - col] and not diag2[row + col]
    
    def place_queen(row):
        if row == n:
            result.append(["".join(row) for row in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                cols[col] = diag1[row - col] = diag2[row + col] = True
                place_queen(row + 1)
                board[row][col] = "."
                cols[col] = diag1[row - col] = diag2[row + col] = False
    
    result = []
    board = [["."] * n for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    place_queen(0)
    return result

# Example usage
print(solve_n_queens(4))
```

**Time Complexity**: O(n!), as each row has up to `n` options, but many options are pruned.

---

### 4. **Sudoku Solver**

**Problem**: Fill a partially completed 9x9 Sudoku board, ensuring each row, column, and 3x3 sub-box contains unique digits from 1 to 9.

**Solution Approach**:
- Use backtracking to try each number in each empty cell.
- If the board remains valid, proceed to the next empty cell; otherwise, backtrack.

**Code Example**:

```python
def solve_sudoku(board):
    def is_valid(row, col, num):
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        return not (num in rows[row] or num in cols[col] or num in boxes[box_row + box_col])

    def place_num(row, col, num):
        board[row][col] = str(num)
        rows[row].add(num)
        cols[col].add(num)
        boxes[3 * (row // 3) + col // 3].add(num)

    def remove_num(row, col, num):
        board[row][col] = '.'
        rows[row].remove(num)
        cols[col].remove(num)
        boxes[3 * (row // 3) + col // 3].remove(num)

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            place_num(i, j, num)
                            if backtrack():
                                return True
                            remove_num(i, j, num)
                    return False
        return True

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = int(board[i][j])
                place_num(i, j, num)
    
    backtrack()
```

---

### Summary of Backtracking

| **Problem**           | **Complexity** | **Explanation**                                                  |
|-----------------------|----------------|------------------------------------------------------------------|
| **Permutations**      | O(n * n!)      | Generates all possible orderings of the elements.                |
| **Subsets**           | O(2^n)         | Each element has two options: included or excluded.              |
| **N-Queens**          | O(n!)          | Places queens row by row while checking for conflicts.           |
| **Sudoku Solver**     | O(9^(n))       | Backtracking approach to fill cells, `n` is the number of blanks.|

Backtracking is powerful but can be computationally expensive. It’s best for problems where an exhaustive search is required, and pruning branches of the search tree early can drastically improve performance.