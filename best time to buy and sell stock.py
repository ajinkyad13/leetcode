# idea is to maintain a currMin and maxProf, if current element is less than currMin, make the current element as currMin
# check if curr element - currMin is higher than maxProf, if yes update the maxProf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        currMin = float("inf")
        
        for each in prices:
            if each  < currMin:
                currMin = each
            if each - currMin > maxProf:
                maxProf = each - currMin
        return maxProf
    
# time : O(N) ~ to iterate  over all the prices 
# space : O(1) constant space is used here