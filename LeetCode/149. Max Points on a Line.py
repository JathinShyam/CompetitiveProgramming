"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.

"""
class Solution:
    def maxPoints(self, points):

        def calculate_gcd(a, b):
            return a if b == 0 else calculate_gcd(b, a % b)
      
        N = len(points)
        lines = 1

        for i in range(N):
            x1, y1 = points[i]
            slopes = Counter()
            for j in range(i+1, N):
                x2, y2 = points[j]
                delta_x = x2 - x1
                delta_y = y2 - y1
                gcd = calculate_gcd(delta_x, delta_y)

                slope = (delta_x // gcd, delta_y // gcd)
                slopes[slope] += 1

                lines = max(lines, slopes[slope]+1)
        return lines

