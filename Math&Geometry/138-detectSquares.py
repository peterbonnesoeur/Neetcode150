
# To redo
class CountSquares:

    def __init__(self):
        self.grid = dict()
        self.pts = []
        

    def add(self, point: List[int]) -> None:
        self.grid[tuple(point)] = self.grid.get(tuple(point), 0) + 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        # We only care about the opporsite side. If the opposite side is present, 
        # then, we can use the other edges as multiplication factors
        for x, y in self.pts:
            if (abs(x-px) != abs(y-py)) or px == x or py == y:
                continue

            res += self.grid.get((x,py), 0) * self.grid.get((px,y), 0)
        return res