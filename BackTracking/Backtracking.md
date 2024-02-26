# Backtracking
The logic of backtracking, follows a general pattern that can be summarized into the following steps:

### 1. **Choice**:
At each step, you have a set of choices. These could be which element to add to a permutation, which path to take in a maze, which value to assign to a variable in a puzzle, etc. In the permutation example, the choice is which remaining element to add next to the current permutation.

### 2. **Constraints**:
There are constraints that must be respected. In a permutation, a key constraint is that no element can appear more than once. In other types of problems, constraints could be more complex, like the rules of Sudoku, the safe path in a maze, or the valid subset in a combination problem.

### 3. **Goal**:
There is a clear goal to be reached, which determines when a solution is complete. In permutations, the goal is reached when a permutation includes all the original elements exactly once. In other problems, the goal could be reaching the end of a maze, satisfying all conditions of a puzzle, or finding all possible combinations that meet certain criteria.

### Backtracking Process:

1. **Make a Choice**: Select from the available options based on the problem's rules.

2. **Explore**: Move forward with this choice as part of your solution and explore further steps. This typically involves recursive calls, where each call represents a deeper level of choices.

3. **Constraints Check**: Continuously check if the current partial solution respects the problem's constraints. If it violates any constraints, stop exploring this path and go back (backtrack).

4. **Goal Check**: Check if the current partial solution meets the goal. If it does, record the solution or take necessary actions (like adding the solution to a list).

5. **Backtrack**: After exploring all possibilities with the current choice (whether it led to a solution or not), undo the last choice. This means removing the last element added to a permutation, moving back to a previous position in a maze, or unassigning the last variable. Then, return to the previous step in the process to explore new choices.

6. **Iterate**: Continue this process, making new choices and backtracking as necessary until all possible configurations have been explored.

### Summary:
Backtracking is essentially a trial-and-error method. You try different choices, backtrack when a choice leads to a dead end (i.e., it breaks a constraint or there are no more choices to make), and continue trying different paths until you find a solution or confirm that no solution exists. It's a systematic way to go through all possible configurations of a problem space to find all solutions that meet the criteria defined by the constraints and goal of the problem.