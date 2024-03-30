"""
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100

Ref: NeetCode YT
"""

from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Check the occurences of tasks
        count = Counter(tasks)

        # we care about handling the most freqently occured task and rest will sort out automatically.
        # we only care about values and create a min heap of values
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        # create a deque for waiting tasks
        queue = deque() # (taskFreq, readyTime)

        # final result to return
        time = 0

        # if we have pending tasks or waiting queue then we iterate
        while len(heap) > 0 or len(queue) > 0:
            time += 1
            
            # If the heap is not empty
            if heap:
                # we pop the element and increment 1
                val = 1 + heapq.heappop(heap)
                # if task frequency is still there, then send to queue for waiting
                if val:
                    queue.append((val, n + time))
            
            # If the queue element is ready, then we send to heap for next iteration.
            if queue and queue[0][1] == time:
                val, _ = queue.popleft()
                heapq.heappush(heap, val)
        return time