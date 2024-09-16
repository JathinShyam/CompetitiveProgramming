"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".

"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def timeDiff(amins, bmins):
            return min(
                abs(amins - bmins),
                abs(amins + 60 * 24 - bmins),
                abs(amins - (bmins + 60 * 24))
            )

        def minutes(hh, mm):
            return hh * 60 + mm

        N = len(timePoints)
        timePoints.sort()
        best = 10 ** 20
        for i in range(N):
            a = timePoints[i]
            b = timePoints[(i+1) % N]
            ah, am = a.split(':')
            bh, bm = b.split(':')
            amins = minutes(int(ah), int(am))
            bmins = minutes(int(bh), int(bm))
            time = timeDiff(amins, bmins)
            best = min(best, time)
        
        return best
