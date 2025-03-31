class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        # j=0
        # for i in range(0,len(nums)):
        #     if val!=nums[i]:
        #         nums[j]=nums[i]
        #         j+=1
        # return j

        