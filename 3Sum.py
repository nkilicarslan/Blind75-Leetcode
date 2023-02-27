from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create a dict to keep unique items and their count
        nums_dict = {}
        # create a dict to keep tuples
        keep_tuples = {}
        # create a result dict to keep unique triplets
        result = {}
        # create a return list
        res = []
        # iterate over the nums list and update num_dict
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                nums_dict[i] += 1
        # iterate over the nums list and store tuples in the keep_tuples dict
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if ((nums[i], nums[j]) not in keep_tuples) and ((nums[j], nums[i]) not in keep_tuples):
                    keep_tuples[nums[i], nums[j]] = 1
        # iterate over the tuples
        for i in keep_tuples:
            # take the sum of them
            sum = i[0] + i[1]
            # calculate the target value
            target_value = 0 - sum
            # check it is unique or not
            if (target_value in nums_dict) and ((target_value , i[0] , i[1]) not in result) and ((target_value , i[1] , i[0]) not in result) and ((i[0] , target_value , i[1]) not in result) and ((i[0] , i[1] , target_value) not in result) and ((i[1] , i[0] , target_value) not in result) and ((i[1], target_value , i[0]) not in result):
                # create a temp variable in order to check the target value is in the list or not
                tmp_count = 1
                if target_value == i[0]:
                    tmp_count += 1
                if target_value == i[1]:
                    tmp_count += 1
                # if the target value is in the list store the triples both in the res list and result dict
                if nums_dict[target_value] >= tmp_count:
                    result[i[0], i[1], target_value] = 1
                    res.append([i[0], i[1], target_value])
        # return the result list
        return res