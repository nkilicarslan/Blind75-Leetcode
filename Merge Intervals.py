from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # create a result list to store the final result
        result_list = []
        # sort the the list according to first element of the sublist
        intervals.sort(key=lambda x: x[0])
        # create a variable to store new interval
        new_interval = intervals[0]
        # iterate over the intervals
        for i in range(1,len(intervals)):
            # if the old interval is not overlaping the new interval
            if new_interval[1] < intervals[i][0]:
                # append the old interval
                result_list.append(new_interval)
                # assing the new interval
                new_interval = intervals[i]
            # if the two interval is overlapping
            elif new_interval[1] >= intervals[i][0]:
                # take the largerst interval
                new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
        # finally append the last interval
        result_list.append(new_interval)
        # return the result list
        return result_list
