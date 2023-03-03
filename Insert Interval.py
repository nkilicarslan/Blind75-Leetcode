from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # create a result list to store
        result = []
        # iterate over the intervals
        for i in range(len(intervals)):
            # if the new interval is smaller than instant interval
            if newInterval[1] < intervals[i][0]:
                # append the new interval than rest of the interval list
                result.append(newInterval)
                return result + intervals[i:]
            # if the new interval is greater than instant interval
            elif newInterval[0] > intervals[i][1]:
                # append the instant interval to the result list
                result.append(intervals[i])
            else:
                # take minimum and the maximum of the intervals and assign it
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        # at the end append the new interval to the result list.
        result.append(newInterval)
        return result

