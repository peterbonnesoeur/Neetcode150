from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preMap = defaultdict(list)

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        # We use a list AND a set there to have fast checking + ordered results
        visited = set()
        output = []

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
