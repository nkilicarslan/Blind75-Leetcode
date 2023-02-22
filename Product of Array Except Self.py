from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create an variable to keep the total product of the list
        product_of_nums = 1
        # create a result list to store final results
        final_results = []
        # iterate over the array and find the total product
        for i in nums:
            product_of_nums *= i
        # iterate over the list and find the final results with dividing each element to product of nums
        for i in range(len(nums)):
            # if the value is zero, since the number can not be divided to zero, iterate the whole list again then calculate it final product
            if nums[i] == 0:
                # create a temporary result value
                tmp_value = 1
                for j in range(len(nums)):
                    # Every iteration if the value is not itself product them
                    if i == j:
                        continue
                    tmp_value *= nums[j]
                # finally append the final result to final resul list
                final_results.append(tmp_value)
            else:
                # if the value is not zero, just divide the number
                final_results.append(int(product_of_nums/nums[i]))
        return final_results