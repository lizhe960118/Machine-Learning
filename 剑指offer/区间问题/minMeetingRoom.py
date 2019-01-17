# 给定一系列的会议时间间隔，包括起始和结束时间[[s1,e1]，[s2,e2]，…(si < ei)，
# 确定所需要的最小会议室数量

# Definition for an interval
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRoom(self, intervals):
        reIntervals = []
        for interval in intervals:
            # 开始时间标记为1， 结束时间标记为-1
            reIntervals.append([interval.start, 1]) 
            reIntervals.append([interval.end, -1])
        reIntervals.sort(key = lambda x:x[0])

        # 从左到右扫描，ans记录所需的会议室数量，count记录当前和
        ans = 0
        count = 0
        for inter in reIntervals:
            count += inter[1]
            ans = max(ans, count)
        return ans