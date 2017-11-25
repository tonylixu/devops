# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        # We sort the list with the interval's start
        intervals.sort(key=lambda x:x.start)
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            pre, cur = merged_intervals[-1], intervals[i]
            if pre.end >= cur.start:
                pre.end = max(pre.end, cur.end)
            else:
                merged_intervals.append(cur)
        return merged_intervals]
