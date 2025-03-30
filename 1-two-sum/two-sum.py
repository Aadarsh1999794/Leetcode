class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Two Sum
        list2=[]
        hash_map={}
        for i in range(0,len(nums)):
            Temp=target-nums[i]
            if Temp in hash_map:
                list2.extend([hash_map[Temp],i])
                break
            hash_map[nums[i]]=i
        return list2

        