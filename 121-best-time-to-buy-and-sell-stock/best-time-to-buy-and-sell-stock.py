class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ele=prices[0]
        max_prof=0
        if len(prices)==1:
            return 0
        else:
            for i in range(1,len(prices)):
                if prices[i]<min_ele:
                    min_ele=prices[i]
                    continue
                diff=prices[i]-min_ele
                if diff>max_prof:
                    max_prof=diff
        return max_prof






        