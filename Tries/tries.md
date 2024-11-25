# But Jamie, what is a trie?

**Tries**, also known as **prefix trees**, are a special kind of tree used to store collections of strings, such as words or sequences. A trie is often used for searching, auto-completion, spell checking, and other applications where prefixes are involved. In a trie, each node represents a character of a word, and the path from the root to a node forms a word (or part of a word). Let's explore **trie techniques**, key operations, time complexity, and common use cases.

### Structure of a Trie

A trie node typically contains:
1. **Children**: A dictionary (or an array for fixed-size alphabets) that maps characters to child nodes.
2. **End of Word Marker**: A boolean flag to indicate if a node represents the end of a valid word.

Here's the basic structure of a trie node in Python:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
```

---

### 1. **Inserting a Word into a Trie**

To insert a word into a trie, you follow each character of the word, moving down the tree, and create nodes as necessary. After the last character of the word, you mark the node as the end of the word.

#### Example of Insertion:

```python
def insert(self, word):
    current_node = self.root
    for char in word:
        if char not in current_node.children:
            current_node.children[char] = TrieNode()
        current_node = current_node.children[char]
    current_node.is_end_of_word = True
```

**Time Complexity**: O(m), where `m` is the length of the word.
- Each character is inserted one at a time, and creating a new node takes constant time.

---

### 2. **Searching for a Word in a Trie**

To search for a word, you traverse the trie from the root, following each character in the word. If you reach the end of the word and the corresponding node is marked as the end of a valid word, the word exists in the trie.

#### Example of Searching:

```python
def search(self, word):
    current_node = self.root
    for char in word:
        if char not in current_node.children:
            return False
        current_node = current_node.children[char]
    return current_node.is_end_of_word
```

**Time Complexity**: O(m), where `m` is the length of the word.
- Each character is searched one at a time, and finding a child node takes constant time in a hash map or array.

---

### 3. **Starts With (Prefix Search)**

One of the powerful features of a trie is efficiently checking whether any word in the trie starts with a given prefix. This can be done by traversing the trie for the prefix, similar to searching for a word.

#### Example of Prefix Search:

```python
def starts_with(self, prefix):
    current_node = self.root
    for char in prefix:
        if char not in current_node.children:
            return False
        current_node = current_node.children[char]
    return True  # Found all characters of the prefix
```

**Time Complexity**: O(m), where `m` is the length of the prefix.
- Similar to word search, you just need to traverse the trie for the characters in the prefix.

---

### 4. **Trie Deletion**

Trie deletion is trickier than insertion and search. When deleting a word, you need to ensure that no other words in the trie share the prefix of the word you're deleting. If they do, you cannot remove those nodes. 

There are three main cases for deletion:
1. **The word exists, and it is not a prefix for any other word**: In this case, you can safely remove nodes corresponding to the word.
2. **The word exists, but other words share its prefix**: You should only unmark the `is_end_of_word` flag but keep the nodes intact.
3. **The word doesn’t exist**: Do nothing.

#### Example of Deletion:

```python
def delete(self, word):
    def _delete(node, word, depth):
        if depth == len(word):
            if not node.is_end_of_word:
                return False  # Word not found
            node.is_end_of_word = False
            return len(node.children) == 0  # If no children, delete node

        char = word[depth]
        if char not in node.children:
            return False  # Word not found

        should_delete_child = _delete(node.children[char], word, depth + 1)

        if should_delete_child:
            del node.children[char]
            return len(node.children) == 0  # Check if current node should be deleted

        return False

    _delete(self.root, word, 0)
```

**Time Complexity**: O(m), where `m` is the length of the word.
- In the worst case, you traverse the entire word, and in the best case, only part of it (if shared prefixes exist).

---

### 5. **Auto-complete and Prefix-based Suggestions**

One of the most powerful use cases of tries is **auto-complete** or providing **suggestions** for a given prefix. Once you have traversed the trie to the node corresponding to the prefix, you can collect all the words that start with that prefix by performing a **DFS** or **BFS** from that node.

#### Example of Auto-complete:

```python
def find_words_with_prefix(self, prefix):
    def dfs(node, path, result):
        if node.is_end_of_word:
            result.append(path)  # A valid word is found

        for char, next_node in node.children.items():
            dfs(next_node, path + char, result)

    # First, find the node that matches the prefix
    current_node = self.root
    for char in prefix:
        if char not in current_node.children:
            return []  # No words with the given prefix
        current_node = current_node.children[char]

    # Perform DFS from that node to collect all words
    result = []
    dfs(current_node, prefix, result)
    return result
```

**Time Complexity**:
- **O(m)** to find the node corresponding to the prefix, where `m` is the length of the prefix.
- **O(k)** to collect all words with the given prefix, where `k` is the total number of characters in all the words starting with the prefix.

---

### 6. **Counting Words with a Given Prefix**

To count the number of words that start with a given prefix, we traverse the trie to find the node corresponding to the last character of the prefix and then count the words in the subtree rooted at that node.

#### Example of Counting Words with a Prefix:

```python
def count_words_with_prefix(self, prefix):
    def dfs_count(node):
        count = 1 if node.is_end_of_word else 0
        for next_node in node.children.values():
            count += dfs_count(next_node)
        return count

    current_node = self.root
    for char in prefix:
        if char not in current_node.children:
            return 0  # No words with the given prefix
        current_node = current_node.children[char]

    return dfs_count(current_node)
```

**Time Complexity**:
- **O(m)** to find the node corresponding to the prefix, where `m` is the length of the prefix.
- **O(k)** to count the words, where `k` is the number of words starting with the prefix.

---

### 7. **Trie vs. Hash Maps**

While **hash maps** (dictionaries) are often used for storing words and performing lookups, tries provide some distinct advantages:
- **Prefix-based operations** (like auto-complete) are much more efficient in tries. With hash maps, you would have to scan all keys to find matching prefixes, which is O(n). In tries, prefix searches are O(m), where `m` is the length of the prefix.
- **Memory consumption**: In tries, space can be reduced if many words share the same prefix. However, tries can use more space in cases with sparse data.
- **String comparison**: In a hash map, each lookup involves computing the hash of the string, while in a trie, lookup depends on the length of the string but doesn’t require full-string comparisons.

---

### Trie Patterns and Use Cases

1. **Auto-completion**: Finding all valid words based on a given prefix.
2. **Spell Checking**: Quickly verifying if a word is valid or finding suggestions based on a misspelling.
3. **Longest Common Prefix**: Finding the longest common prefix in a set of words.
4. **Word Search on a Grid**: Given a matrix of characters, use a trie to efficiently search for valid words (used in problems like "Word Search II").
5. **Dictionary/Phonebook Applications**: Fast lookups based on partial inputs (e.g., searching for contacts by prefix).

### Summary

| **Operation**      | **Time Complexity** |
|--------------------|---------------------|
| Insert             | O(m)                |
| Search             | O(m)                |
| Starts With (Prefix)| O(m)                |
| Delete             | O(m)                |
| Auto-complete      | O(m + k)            |
| Count Words with Prefix | O(m + k)        |

- `m` is the length of the word or prefix.
- `k` is the total number of characters in all words that match the prefix.

Tries are highly efficient for prefix-based operations, making them valuable in applications like search