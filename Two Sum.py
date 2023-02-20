class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # decleare an array to keep indexes of elements
        indexes = []
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if (nums[i] + nums[j]) == target and i !=j:
                    indexes.clear()
                    indexes.append(min(i,j))
                    indexes.append(max(i,j))
        return indexes