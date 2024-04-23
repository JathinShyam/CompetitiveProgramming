"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.

"""


# Union Find Solution
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
        parent = [x for x in range(N)]

        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]
        
        def uunion(x,y):
            ux = ufind(x)
            uy = ufind(y)
            parent[ux] = uy
        
        def dist(x,y):
            return (abs(points[x][0]-points[y][0]) + abs(points[x][1] - points[y][1]))
        
        for i in range(N):
            for j in range(i+1, N):
                edges.append((dist(i,j), i, j))
        
        edges.sort()

        total = 0
        for cost, x, y in edges:
            if ufind(x) != ufind(y):
                uunion(x,y)
                total += cost
        return total
    

# Prim's Algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges[i].append([dist, j])
                edges[j].append([dist, i])
        
        res = 0
        visited = set()
        minH = [[0, 0]] #[cost, start]
        while len(visited) < N:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for neiCost, neiNode in edges[node]:
                if neiNode not in visited:
                    heapq.heappush(minH, [neiCost, neiNode])
        return res
