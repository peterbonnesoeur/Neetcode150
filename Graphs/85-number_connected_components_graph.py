class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        preMap = defaultdict(list)

        # map each course to : prereq list
        for crs, pre in edges:
            preMap[crs].append(pre)
            preMap[pre].append(crs)

        visited = set()

        def bfs(crs):
            queue = deque()

            queue.append(crs)
            for edge in preMap[crs]:
                queue.append(edge)

            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    bfs(node)

            return
        
        count = 0
        for edge in range(n):
            len_old_visited = len(visited)
            bfs(edge)
            if len_old_visited != len(visited):
                count += 1

        return count
