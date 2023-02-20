class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # decleare an dict to identify numbers
        number_dict = {}

        for i in range(len(nums)):
            if target - nums[i] not in number_dict:
                number_dict[nums[i]] = i
            else:
                return[i,number_dict[target-nums[i]]]