from typing import List
def maxsubarray(self, nums: List[int]) -> int:
    cs = nums[0]
    os = nums[0]
    for i in range(1,len(nums)):
        if cs + nums[i] > i:
           cs = cs + nums[i]
        else:
           cs = nums[i]
        os = max(cs , os)
        return os
