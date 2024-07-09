class Solution:

    ## The basic idea here is to chekc for 2 things for the tree to work:
    # - No loops
    # - No alone edges -> there are 2 graphs in one or no edge is collected


    ## The way that I do here is first to init the neighboors, iterate over them
    ## Then, I check if it was already visited -> False
    ## I also keep track of the imediate parent, in case it is present in the list of inputs, in this case, it gets
    ## a false as well
    ## Finally, I count that all the nodes have been visited.

    def is_tree(self, graph, n):
        # graph is represented as an adjacency list
        visited = [False] * n

        def dfs(node, parent):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if not dfs(neighbor, node):
                        return False
                elif neighbor != parent:
                    return False
            return True

        # Start DFS from the first node (assuming nodes are labeled from 0 to n-1)
        if not dfs(0, -1):
            return False

        # Check for connectivity
        if not all(visited):
            return False

        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        return self.is_tree(graph, n)
