# But Jamie, what is a trie?

A trie, also known as a prefix tree or digital tree, is a type of search tree used to store a dynamic set or associative array where the keys are usually strings. Unlike a binary search tree, where node in the tree stores a key, in a trie, the position in the tree defines the key with which it is associated, making it a very efficient data structure for certain kinds of search purposes, especially in scenarios involving large datasets of strings. Here’s how it works and why it’s useful:

### Structure:

1. **Nodes:** Each node of the trie represents a single character of a string. The root node represents an empty value or the start of a word.

2. **Edges/Links:** Each node in the trie can have as many children as there are possible characters in the dataset. For example, if the trie stores lower case English letters, each node could have up to 26 children, one for each letter.

3. **End of Word:** A marker or flag (often a special field or value) is used to indicate the end of a word within the trie. This allows the trie to distinguish between keys that are prefixes of longer keys.

### Advantages:

1. **Efficiency:** Retrieval of a key can be performed in \(O(m)\) time, where \(m\) is the length of the key. This makes tries particularly efficient for lookup-intensive applications.

2. **Prefix Matching:** Tries are excellent for prefix matching, as they allow you to retrieve all keys that share a common prefix, which is a common requirement in auto-complete systems.

3. **Space Saving:** While the worst-case space complexity can be high (especially for a sparse trie), tries can be space-efficient when storing a large set of strings that share common prefixes, since common prefixes are stored only once.

### Usage:

Tries are widely used in applications such as:

- Autocomplete features in search engines or text editors.
- Spell checkers and dictionary implementations.
- IP routing algorithms.
- Pattern matching algorithms, especially in bioinformatics for matching DNA sequences.

A simple example of a trie could be the storage of the set of strings ["fun", "function", "factory"]. In this trie, the common prefixes "fun" of "fun" and "function" would be shared, meaning that the characters 'f', 'u', and 'n' are stored only once at the beginning of the trie to represent both words until they diverge.