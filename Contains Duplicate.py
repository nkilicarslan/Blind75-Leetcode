class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create an dict to check whether number in array twice or not
        num_dict = {}
        # iterate over the list and store in the dict
        for i in range(len(nums)):
            # check the duplicate, if the dict contains return True
            if nums[i] in num_dict:
                return True
            else:
                num_dict[nums[i]] = 1
        # If the list contains no duplicate return False
        return False