# 给定一系列的会议时间间隔，包括起始和结束时间[[s1,e1]，[s2,e2]，…(si < ei)，
# 确定一个人是否可以参加所有会议。

# Definition for an interval
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeeting(self, intervals):
        intervals.sort(key=lambda x:x.start)
        n = len(intervals)

        # for i in range(n - 1):
        #     if intervals[i].end > intervals[i + 1].start:
        #         return False

        end = -1
        for inter in intervals:
            if inter.start > end:
                end = inter.end
            else:
                return False

        return True
