# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def mergeIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x:x.start)
        # for obj in intervals:
        #     print(obj.start)
        n = len(intervals)
        if n <= 1:
            return intervals
        ans = [intervals[0]]
        for i in range(1, n):
            ans = ans[:-1] + self.merge_helper(ans[-1], intervals[i])
        return ans
    def merge_helper(self, a, b):
        if a.end >= b.start:
            return [Interval(a.start, max(a.end,b.end))]
        else:
            return [a, b]