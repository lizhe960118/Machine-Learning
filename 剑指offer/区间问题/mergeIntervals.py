# 给定一系列的间隔,合并重合的区间

# Definition for an interval
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeeting(self, intervals):
        intervals.sort(key=lambda x:x.start)
        n = len(intervals)

        ret = []
        for i in range(n):
            if ret == []:
                ret.append(intervals[i])
            else:
                if intervals[i].start <= ret[-1].end:
                    ret[-1].end = max(ret[-1].end, intervals[i].end)
                else:
                    ret.append(intervals[i])

        return ret